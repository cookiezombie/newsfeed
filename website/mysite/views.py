from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import feedparser

def index(request):
     a = feedparser.parse('https://feeds.npr.org/1001/rss.xml')
     b = f"{a.entries[0].title + '. ' + a.entries[0].summary}"
     c = f"{a.entries[1].title + '. ' + a.entries[1].summary}"
     d = f"{a.entries[2].title + '. ' + a.entries[2].summary}"
     e = f"{a.entries[3].title + '. ' + a.entries[3].summary}"
     ef = f"{a.entries[4].title + '. ' + a.entries[4].summary}"
     g = f"{a.entries[5].title + '. ' + a.entries[5].summary}"
     h = f"{a.entries[6].title + '. ' + a.entries[6].summary}"
     i = f"{a.entries[7].title + '. ' + a.entries[7].summary}"
     j = f"{a.entries[8].title + '. ' + a.entries[8].summary}"
     k = f"{a.entries[9].title + '. ' + a.entries[9].summary}"
     l = f"{a.entries[10].title + '. ' + a.entries[10].summary}"
     m = f"{a.entries[11].title + '. ' + a.entries[11].summary}"
     n = f"{a.entries[12].title + '. ' + a.entries[12].summary}"
     o = f"{a.entries[13].title + '. ' + a.entries[13].summary}"
     p = f"{a.entries[14].title + '. ' + a.entries[14].summary}"
     q = feedparser.parse('https://feeds.arstechnica.com/arstechnica/index')
     r = f"{q.entries[0].title + '. ' + q.entries[0].summary}"
     s = f"{q.entries[1].title + '. ' + q.entries[1].summary}"
     t = f"{q.entries[2].title + '. ' + q.entries[2].summary}"
     u = f"{q.entries[3].title + '. ' + q.entries[3].summary}"
     v = f"{q.entries[4].title + '. ' + q.entries[4].summary}"
     w = f"{q.entries[5].title + '. ' + q.entries[5].summary}"
     x = f"{q.entries[6].title + '. ' + q.entries[6].summary}"
     y = f"{q.entries[7].title + '. ' + q.entries[7].summary}"
     z = f"{q.entries[8].title + '. ' + q.entries[8].summary}"
     ab = f"{q.entries[9].title + '. ' + q.entries[9].summary}"
     ac = f"{q.entries[10].title + '. ' + q.entries[10].summary}"
     ad = f"{q.entries[11].title + '. ' + q.entries[11].summary}"
     ae = f"{q.entries[12].title + '. ' + q.entries[12].summary}"
     af = f"{q.entries[13].title + '. ' + q.entries[13].summary}"
     ag = f"{q.entries[14].title + '. ' + q.entries[14].summary}"
     ah = feedparser.parse('https://www.wgrz.com/feeds/syndication/rss/news/local')
     ai = f"{ah.entries[0].title + '. ' + ah.entries[0].summary}"
     aj = f"{ah.entries[1].title + '. ' + ah.entries[1].summary}"
     ak = f"{ah.entries[2].title + '. ' + ah.entries[2].summary}"
     al = f"{ah.entries[3].title + '. ' + ah.entries[3].summary}"
     am = f"{ah.entries[4].title + '. ' + ah.entries[4].summary}"
     an = f"{ah.entries[5].title + '. ' + ah.entries[5].summary}"
     ao = f"{ah.entries[6].title + '. ' + ah.entries[6].summary}"
     ap = f"{ah.entries[7].title + '. ' + ah.entries[7].summary}"
     aq = f"{ah.entries[8].title + '. ' + ah.entries[8].summary}"
     ar = f"{ah.entries[9].title + '. ' + ah.entries[9].summary}"
     return render(request, 'mysite/index.html', {'b':b,'c':c,'d':d,'e':e,'ef':ef,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,'y':y,'z':z,'ab':ab,'ac':ac,'ad':ad,'ae':ae,'af':af,'ag':ag,'ai':ai,'aj':aj,'ak':ak,'al':al,'am':am,'an':an,'ao':ao,'ap':ap,'aq':aq,'ar':ar})

def news(request):
     za = feedparser.parse('https://feeds.npr.org/1001/rss.xml')
     zb = {0: f"{za.entries[0].title + '. ' + za.entries[0].summary}"}
     zc = {1: f"{za.entries[1].title + '. ' + za.entries[1].summary}"}
     zd = {2: f"{za.entries[2].title + '. ' + za.entries[2].summary}"}
     ze = {3: f"{za.entries[3].title + '. ' + za.entries[3].summary}"}
     zf = {4: f"{za.entries[4].title + '. ' + za.entries[4].summary}"}
     zg = {5: f"{za.entries[5].title + '. ' + za.entries[5].summary}"}
     zh = {6: f"{za.entries[6].title + '. ' + za.entries[6].summary}"}
     zi = {7: f"{za.entries[7].title + '. ' + za.entries[7].summary}"}
     zj = {8: f"{za.entries[8].title + '. ' + za.entries[8].summary}"}
     zk = {9: f"{za.entries[9].title + '. ' + za.entries[9].summary}"}
     zl = {10: f"{za.entries[10].title + '. ' + za.entries[10].summary}"}
     zm = {11: f"{za.entries[11].title + '. ' + za.entries[11].summary}"}
     zn = {12: f"{za.entries[12].title + '. ' + za.entries[12].summary}"}
     zo = {13: f"{za.entries[13].title + '. ' + za.entries[13].summary}"}
     zp = {14: f"{za.entries[14].title + '. ' + za.entries[14].summary}"}
     zq = feedparser.parse('https://feeds.arstechnica.com/arstechnica/index')
     zr = {15: f"{zq.entries[0].title + '. ' + zq.entries[0].summary}"}
     zs = {16: f"{zq.entries[1].title + '. ' + zq.entries[1].summary}"}
     zt = {17: f"{zq.entries[2].title + '. ' + zq.entries[2].summary}"}
     zu = {18: f"{zq.entries[3].title + '. ' + zq.entries[3].summary}"}
     zv = {19: f"{zq.entries[4].title + '. ' + zq.entries[4].summary}"}
     zw = {20: f"{zq.entries[5].title + '. ' + zq.entries[5].summary}"}
     zx = {21: f"{zq.entries[6].title + '. ' + zq.entries[6].summary}"}
     zy = {22: f"{zq.entries[7].title + '. ' + zq.entries[7].summary}"}
     zz = {23: f"{zq.entries[8].title + '. ' + zq.entries[8].summary}"}
     zza = {24: f"{zq.entries[9].title + '. ' + zq.entries[9].summary}"}
     zzb = {25: f"{zq.entries[10].title + '. ' + zq.entries[10].summary}"}
     zzc = {26: f"{zq.entries[11].title + '. ' + zq.entries[11].summary}"}
     zzd = {27: f"{zq.entries[12].title + '. ' + zq.entries[12].summary}"}
     zze = {28: f"{zq.entries[13].title + '. ' + zq.entries[13].summary}"}
     zzf = {29: f"{zq.entries[14].title + '. ' + zq.entries[14].summary}"}
     zzg = feedparser.parse('https://www.wgrz.com/feeds/syndication/rss/news/local')
     zzh = {30: f"{zzg.entries[0].title + '. ' + zzg.entries[0].summary}"}
     zzi = {31: f"{zzg.entries[1].title + '. ' + zzg.entries[1].summary}"}
     zzj = {32: f"{zzg.entries[2].title + '. ' + zzg.entries[2].summary}"}
     zzk = {33: f"{zzg.entries[3].title + '. ' + zzg.entries[3].summary}"}
     zzl = {34: f"{zzg.entries[4].title + '. ' + zzg.entries[4].summary}"}
     zzm = {35: f"{zzg.entries[5].title + '. ' + zzg.entries[5].summary}"}
     zzn = {36: f"{zzg.entries[6].title + '. ' + zzg.entries[6].summary}"}
     zzo = {37: f"{zzg.entries[7].title + '. ' + zzg.entries[7].summary}"}
     zzp = {38: f"{zzg.entries[8].title + '. ' + zzg.entries[8].summary}"}
     zzq = {39: f"{zzg.entries[9].title + '. ' + zzg.entries[9].summary}"}
     return JsonResponse([zb,zc,zd,ze,zf,zg,zh,zi,zj,zk,zl,zm,zn,zo,zp,zr,zs,zt,zu,zv,zw,zx,zy,zz,zza,zzb,zzc,zzd,zze,zzf,zzh,zzi,zzj,zzk,zzl,zzm,zzn,zzo,zzp,zzq],safe=False)
