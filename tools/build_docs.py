#!/usr/bin/env python3
"""Rebuild AQL, Markdown, SVG and three localized PDFs from public catalogs."""
from pathlib import Path
import html
import json
import re
import sys
from xml.sax.saxutils import escape
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from fieldbook import load_catalog, read_json, query_file_text

LABELS={
'en':dict(manual='Field manual',usage='Using the repository',advanced='Advanced queries and performance',need='Prerequisites',read='Read the result',limit='Limits and false positives',fast='Reduce search work',refs='References',query='Query',quick='Quick start',files='File map',props='Custom-property mapping',sources='Sources',index='Query index',status='Offline template; not executed on Ariel.',diagram='Conceptual model - not a physical query execution plan',nav='Contents',clause='Worked reading',variant='Optimization variants',language='English',chapter='CHAPTER'),
'it':dict(manual='Manuale operativo',usage='Uso del repository',advanced='Query avanzate e prestazioni',need='Prerequisiti',read='Leggere il risultato',limit='Limiti e falsi positivi',fast='Ridurre il lavoro di ricerca',refs='Riferimenti',query='Query',quick='Avvio rapido',files='Mappa dei file',props='Mappatura delle proprietà custom',sources='Fonti',index='Indice delle query',status='Template offline; non eseguito su Ariel.',diagram='Modello concettuale - non è un execution plan fisico',nav='Contenuti',clause='Lettura guidata',variant='Varianti di ottimizzazione',language='Italiano',chapter='CAPITOLO')}
DIAGRAMS={
'en':{'workflow':['Extract and verify','Set parameters','Render locally','Review fields','Run in QRadar'],'scope':['Time + indexed scope','Candidate filtering','Group and sort','Transfer + review'],'subquery':['Recent failure users','Membership set','Success events','No order imposed'],'baseline':['Prior snapshot','Current contacts','Compare membership','Review new contacts'],'evidence':['Request or header','Process and file','Network evidence','Correlated timeline'],'aggregate':['Selected records','Group dimensions','Weighted measures','Interpret context'],'timeline':['Observe timestamps','Check clock/collector','Deduplicate sessions','Review intervals']},
'it':{'workflow':['Estrai e verifica','Imposta parametri','Genera offline','Controlla campi','Esegui in QRadar'],'scope':['Tempo + scope indicizzato','Filtra i candidati','Raggruppa e ordina','Trasferisci e leggi'],'subquery':['Utenti con errori','Set di appartenenza','Eventi di successo','Ordine non imposto'],'baseline':['Snapshot precedente','Contatti correnti','Confronta appartenenza','Verifica le novità'],'evidence':['Richiesta o header','Processo e file','Evidenza di rete','Timeline correlata'],'aggregate':['Record selezionati','Dimensioni del gruppo','Misure pesate','Interpreta il contesto'],'timeline':['Osserva i timestamp','Verifica clock/collector','Deduplica sessioni','Esamina intervalli']}}

def wrap_sql(text,width=76):
    result=[]
    for original in text.splitlines():
        line=original
        while len(line)>width:
            quoted=False;double=False;points=[]
            for i,c in enumerate(line[:width+1]):
                if c=="'" and not double:quoted=not quoted
                elif c=='"' and not quoted:double=not double
                elif c==' ' and not quoted and not double and i>15:points.append(i)
            if not points:break
            pos=points[-1];result.append(line[:pos]);line='       '+line[pos+1:].lstrip()
        result.append(line)
    return '\n'.join(result)

def svg_diagram(kind,lang):
    labels=DIAGRAMS[lang][kind];n=len(labels);box=210;gap=33;width=n*(box+gap)+27
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="176" viewBox="0 0 {width} 176" role="img" aria-label="{escape(kind)}">',f'<rect width="{width}" height="176" rx="16" fill="#edf5f6"/>']
    for i,word in enumerate(labels):
        x=25+i*(box+gap)
        parts.append(f'<rect x="{x}" y="38" width="{box}" height="68" rx="8" fill="#fff" stroke="#007f83" stroke-width="2"/>')
        parts.append(f'<text x="{x+box/2}" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#102c42">{escape(word)}</text>')
        if i<n-1:
            a=x+box+5;parts.append(f'<path d="M{a} 72h21m-5-5 5 5-5 5" fill="none" stroke="#007f83" stroke-width="2"/>')
    parts.append(f'<text x="25" y="145" font-family="Arial,sans-serif" font-size="12" fill="#52606a">{escape(LABELS[lang]["diagram"])}</text></svg>')
    return '\n'.join(parts)

def markdown_documents(d,qs,vs,lang):
    lab=LABELS[lang];docs=ROOT/'docs';docs.mkdir(exist_ok=True)
    manual=['# '+lab['manual'],'',d['intro'],'',d['status'],'']
    for title,text in d['core_intro']:manual.extend(['## '+title,'',text,''])
    for x in qs:
        manual.extend([f'<a id="{x["id"].lower()}"></a>',f'## {x["id"]} - {x["title"]}','',x['section']+' / '+x['level']+' / '+x['cost'],'',f'**{lab["need"]}:** '+x['need'],'','```sql',x['sql'],'```','',f'**{lab["read"]}:** '+x['interpretation'],'',f'**{lab["limit"]}:** '+x['limitation'],'',f'**{lab["fast"]}:** '+x['performance_note'],'',f'**{lab["refs"]}:** '+x['refs'],''])
    (docs/'manual.md').write_text('\n'.join(manual),encoding='utf-8')
    idx=['# '+lab['index'],'','| ID | '+lab['query']+' |','|---|---|']
    for x in qs+vs:idx.append(f'| [{x["id"]}](../queries/{x["id"]}.aql) | {x["title"]} |')
    (docs/'query-index.md').write_text('\n'.join(idx)+'\n',encoding='utf-8')
    for key,name,title in [('getting','getting-started.md',lab['usage']),('performance','performance.md',lab['advanced']),('publishing','publishing.md','GitHub')]:
        lines=['# '+title,'',d['status'] if key=='getting' else '']
        for a,b in d[key]:lines.extend(['','## '+a,'',b])
        if key=='getting':lines.extend(['','```bash','python3 verify_package.py','python3 render_query.py --list','python3 render_query.py Q001 --params examples/params.ip.json --output work/Q001.aql','```','','```powershell','py -3 -X utf8 verify_package.py','py -3 -X utf8 render_query.py Q001 --params examples/params.ip.json --output work/Q001.aql','```'])
        if key=='publishing':lines.extend(['','```bash','python3 verify_package.py','python3 -m unittest discover -s tests -v','git init -b main','git add .','git commit -m "Release v2.0.0"','git remote add origin https://github.com/OWNER/REPOSITORY.git','git remote -v','git push -u origin main','```','','OWNER/REPOSITORY: '+('replace with your actual empty repository.' if lang=='en' else 'sostituisci con il tuo repository vuoto.'),'','[GitHub documentation](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)'])
        if key=='performance':
            for v in vs:lines.extend(['','## '+v['id']+' - '+v['title'],'','```sql',v['sql'],'```','',v['note']])
        (docs/name).write_text('\n'.join(lines)+'\n',encoding='utf-8')
    atlas=['# '+lab['advanced'],'',d['status']]
    for ident,q,kind,title,text,lim in d['atlas']:
        x=next(z for z in qs if z['id']==q)
        atlas.extend(['','## '+ident+' / '+q+' - '+title,'',f'![{kind}](assets/{kind}.svg)','',text,'','```sql',x['sql'],'```','',f'**{lab["limit"]}:** '+lim,'',f'**{lab["fast"]}:** '+x['performance_note']])
    (docs/'advanced-guide.md').write_text('\n'.join(atlas)+'\n',encoding='utf-8')
    rows=['# '+lab['files'],'','| File | '+('Purpose' if lang=='en' else 'Uso')+' |','|---|---|']+[f'| {a} | {b} |' for a,b in d['filemap']]
    (docs/'file-map.md').write_text('\n'.join(rows)+'\n',encoding='utf-8')
    custom=sorted(set(re.findall(r'"(Hunt_\w+)"',' '.join(x['sql'] for x in qs))))
    prop=['# '+lab['props'],'',d['properties_intro'],'','| '+('Property | Type / meaning' if lang=='en' else 'Proprietà | Tipo / significato')+' |','|---|---|']
    descriptions={'Hunt_Action':('String: canonical allow/deny/drop/blocked values','Stringa: valori canonici allow/deny/drop/blocked'),'Hunt_EventID':('String Windows EventID from the correct provider/channel','Stringa Windows EventID del provider/canale corretto'),'Hunt_TargetUser':('Target identity, separate from initiator','Soggetto dell’operazione, distinto dall’attore'),'Hunt_Status':('HTTP status stored as a string','HTTP status come stringa'),'Hunt_DNSRcode':('Canonical string, e.g. NXDOMAIN','Stringa canonica, es. NXDOMAIN'),'Hunt_SessionID':('Scoped session identifier; protect tokens','Identificatore sessione con scope; proteggere i token')}
    for f in custom:
        note=descriptions.get(f,('String or a locally documented compatible type; verify extraction and NULL behavior','Stringa o tipo compatibile documentato localmente; verificare estrazione e NULL'))[0 if lang=='en' else 1]
        prop.append(f'| {f} | {note} |')
    (docs/'custom-properties.md').write_text('\n'.join(prop)+'\n',encoding='utf-8')
    bench=['# '+d['benchmark_title'],'','| '+('Trial | A duration + unit | B duration + unit | Status | Equivalent results?' if lang=='en' else 'Prova | Durata A + unità | Durata B + unità | Stato | Risultati equivalenti?')+' |','|---|---|---|---|---|','| 1 | | | | |','| 2 | | | | |','| 3 | | | | |','','START / STOP / timezone:','','Sources / domains:','','Indices / historical coverage:','','Cache / load / trial order:','','Median A / Median B / A:B speedup:','','Scope differences / validation date:','']
    (docs/'benchmark-template.md').write_text('\n'.join(bench),encoding='utf-8')
    ss=read_json(ROOT/'sources.json');lines=['# '+lab['sources'],'']
    for x in ss:lines.extend([f'## {x["id"]} - {x["title"]}','',x['url'] or '',x['note'],''])
    (docs/'sources.md').write_text('\n'.join(lines),encoding='utf-8')
    for kind in DIAGRAMS[lang]:(docs/'assets'/f'{kind}.svg').write_text(svg_diagram(kind,lang),encoding='utf-8')


def build_pdfs(d,qs,vs,lang):
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted, Flowable, Table, TableStyle, KeepTogether
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    lab=LABELS[lang];navy=colors.HexColor('#102c42');teal=colors.HexColor('#007f83');pale=colors.HexColor('#edf5f6');grey=colors.HexColor('#52606a')
    w,h=419.5276,595.2756;cw=w-64
    st={
    'h':ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=19,leading=23,textColor=navy,spaceAfter=15),
    'b':ParagraphStyle('b',fontName='Helvetica',fontSize=9.1,leading=13,textColor=navy,spaceAfter=8),
    's':ParagraphStyle('s',fontName='Helvetica',fontSize=7.4,leading=10.5,textColor=grey,spaceAfter=5),
    'sub':ParagraphStyle('sub',fontName='Helvetica-Bold',fontSize=8.7,leading=11.5,textColor=teal,spaceBefore=8,spaceAfter=4),
    'code':ParagraphStyle('code',fontName='Courier',fontSize=7.5,leading=10.3,textColor=navy,spaceBefore=7,spaceAfter=9)}
    def p(t,k='b'):return Paragraph(html.escape(str(t)),st[k])
    def head(t,key):
        f=p(t,'h');f.anchor=key;f.label=t;return f
    def sql(t):return Preformatted(wrap_sql(t),st['code'])
    class Diagram(Flowable):
        def __init__(self,kind):Flowable.__init__(self);self.width=cw;self.height=138;self.kind=kind
        def draw(self):
            c=self.canv;c.setFillColor(pale);c.roundRect(0,0,cw,138,7,fill=1,stroke=0)
            labels=DIAGRAMS[lang][self.kind]
            if len(labels)==5:labels=labels[:3]+[labels[3]+' / '+labels[4]]
            coords=[(12,78),(195,78),(12,17),(195,17)]
            for (x,y),label in zip(coords,labels):
                c.setFillColor(colors.white);c.setStrokeColor(teal);c.roundRect(x,y,149,42,5,fill=1,stroke=1)
                a=p(label,'s');aw,ah=a.wrap(132,40);a.drawOn(c,x+8,y+(42-ah)/2)
            c.setStrokeColor(teal)
            for x1,y1,x2,y2 in [(165,99,191,99),(269,74,269,62),(165,38,191,38)]:
                c.line(x1,y1,x2,y2)
            c.setFillColor(teal);c.setFont('Helvetica',7);c.drawString(12,4,'MODEL / '+self.kind.upper())
    class Doc(SimpleDocTemplate):
        def afterFlowable(self,f):
            if hasattr(f,'anchor'):
                self.canv.bookmarkPage(f.anchor);self.canv.addOutlineEntry(f.label,f.anchor,0,False)
    def foot(c,doc):
        c.saveState();c.setStrokeColor(teal);c.line(32,32,w-32,32);c.setFillColor(grey);c.setFont('Helvetica',6);c.drawString(32,20,'QRADAR BLUE TEAM FIELDBOOK / 2.0.0 / '+lang.upper());c.drawRightString(w-32,20,str(doc.page));c.restoreState()
    def write(name,story):
        target=ROOT/'docs'/'pdf'/name
        doc=Doc(str(target),pagesize=(w,h),leftMargin=32,rightMargin=32,topMargin=33,bottomMargin=45,title='QRadar Blue Team Fieldbook - '+name,author='QRadar Blue Team Fieldbook contributors',pageCompression=1)
        doc.build(story,onFirstPage=foot,onLaterPages=foot)
    def cover(title,tag):return [Spacer(1,26),p('QRADAR / BLUE TEAM','sub'),head(title,tag+'cover'),p(d['tagline']),Diagram('workflow'),Spacer(1,15),p('Public edition 2.0.0 / '+lab['language'],'sub'),p(d['status'],'s'),PageBreak()]
    manual=cover(lab['manual'],'manual')
    for i,(a,b) in enumerate(d['core_intro']):manual.extend([head(a,'intro'+str(i)),p(b),Diagram('scope' if i==7 else 'evidence' if i==4 else 'workflow'),Spacer(1,14),p(d['status'],'s'),PageBreak()])
    for start in range(0,len(qs),20):
        manual.append(head(lab['index'],'index'+str(start)))
        for x in qs[start:start+20]:manual.append(Paragraph(f'<link href="#{x["id"]}" color="#007f83"><b>{x["id"]}</b> {html.escape(x["title"])}</link>',st['b']))
        manual.append(PageBreak())
    for x in qs:
        manual.extend([head(x['id']+' / '+x['title'],x['id']),p(x['section']+' / '+x['level']+' / '+x['cost'],'s'),p(lab['need'],'sub'),p(x['need'],'s'),sql(x['sql']),p(lab['read'],'sub'),p(x['interpretation']),p(lab['limit'],'sub'),p(x['limitation']),p(lab['fast'],'sub'),p(x['performance_note'],'s'),p(lab['refs']+': '+x['refs'],'s'),PageBreak()])
    manual.append(head(lab['sources'],'manualsources'))
    for x in read_json(ROOT/'sources.json'):
        b=[p(x['id']+' / '+x['title'],'sub'),p(x['note'],'s')]
        if x['url']:b.append(Paragraph(f'<link href="{html.escape(x["url"])}" color="#007f83">{html.escape(x["url"].split("/")[2])}</link>',st['s']))
        manual.extend([KeepTogether(b),Spacer(1,5)])
    write('field-manual.pdf',manual)
    advanced=cover(lab['advanced'],'advanced')
    for ident,q,kind,title,text,lim in d['atlas']:
        x=next(z for z in qs if z['id']==q)
        advanced.extend([head(ident+' / '+q+' - '+title,'adv'+ident),Diagram(kind),Spacer(1,12),p(text),p(lab['limit'],'sub'),p(lim),p(lab['fast'],'sub'),p(x['performance_note']),PageBreak(),head(q+' / '+lab['clause'],'adetail'+ident),sql(x['sql']),p(lab['need'],'sub'),p(x['need']),p(lab['read'],'sub'),p(x['interpretation']),p(lab['refs']+': '+x['refs'],'s'),PageBreak()])
    for i,(a,b) in enumerate(d['performance']):advanced.extend([head(a,'perf'+str(i)),Diagram('scope' if i<5 else 'aggregate'),Spacer(1,12),p(b),p(d['status'],'s'),PageBreak()])
    for x in vs:advanced.extend([head(x['id']+' / '+x['title'],x['id']),sql(x['sql']),p(x['note']),p(d['status'],'s'),PageBreak()])
    write('advanced-performance.pdf',advanced)
    use=cover(lab['usage'],'usage')
    linux='python3 verify_package.py\npython3 render_query.py --list\npython3 render_query.py Q001 \\\n  --params examples/params.ip.json \\\n  --output work/Q001.aql'
    windows='py -3 -X utf8 verify_package.py\npy -3 -X utf8 render_query.py Q001 `\n  --params examples/params.ip.json `\n  --output work/Q001.aql'
    for i,(a,b) in enumerate(d['getting']):
        use.extend([head(a,'usage'+str(i)),p(b)])
        if i==2:use.append(sql(linux))
        elif i==3:use.append(sql(windows))
        elif i==4:use.append(sql(json.dumps(read_json(ROOT/'examples'/'params.window.json'),indent=2)))
        elif i==5:use.append(sql('python3 render_query.py Q001 --show'))
        else:use.append(Diagram('workflow' if i<5 else 'evidence'))
        use.extend([Spacer(1,12),p(d['status'],'s'),PageBreak()])
    use.append(head(lab['files'],'usagefiles'))
    for a,b in d['filemap']:use.extend([p(a,'sub'),p(b,'s')])
    use.append(PageBreak())
    for i,(a,b) in enumerate(d['publishing']):
        use.extend([head(a,'publish'+str(i)),p(b)])
        if i==3:use.append(sql('git init -b main\ngit add .\ngit commit -m "Release v2.0.0"'))
        elif i==4:use.append(sql('git remote add origin https://github.com/OWNER/REPOSITORY.git\ngit remote -v\ngit push -u origin main'))
        else:use.append(Diagram('workflow'))
        use.extend([p(d['status'],'s'),PageBreak()])
    write('getting-started.pdf',use)

def main():
    config=read_json(ROOT/'project.json');lang=config['language'];d=read_json(ROOT/'docs'/'content.json')
    qs=read_json(ROOT/'queries.json');vs=read_json(ROOT/'variants.json')
    for path in [ROOT/'queries',ROOT/'docs'/'assets',ROOT/'docs'/'pdf']:path.mkdir(parents=True,exist_ok=True)
    for x in qs+vs:(ROOT/'queries'/(x['id']+'.aql')).write_text(query_file_text(x),encoding='utf-8',newline='\n')
    markdown_documents(d,qs,vs,lang)
    build_pdfs(d,qs,vs,lang)
    print('Built: 117 AQL files, Markdown, SVG and three PDFs. Refresh the manifest explicitly after reviewing changes.')
if __name__=='__main__':main()
