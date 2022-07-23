from siteapp.models import Site

def adding():
    context={
        'ایرنا':'https://www.irna.ir/archive?tp=15',
        'خبرورزشی':'https://www.khabarvarzeshi.com/service/allnews',
        'فوتبالی':'https://footballi.net/news/latest/',
        'فارس':'https://www.farsnews.ir/mainsports',
        'ورزش سه':'https://www.varzesh3.com/news?SportType=1',
        'خبرآنلاین':'https://www.khabaronline.ir/archive?tp=6',
        'تسنیم':'https://www.tasnimnews.com/fa/service/3/%D9%88%D8%B1%D8%B2%D8%B4%DB%8C',
        'ایلنا':'https://www.ilna.ir/newsstudios/archive/?curp=1&categories=7&order=order_time&page=2&curps=1',
        'مهر':'https://www.mehrnews.com/archive?tp=9',
        'ایسنا':'https://www.isna.ir/archive?tp=24',
        'ایمنا':'https://www.imna.ir/service/sport/Football',

    }
    for sname,surl in context.items():
        try:
            Site.objects.get(site_url=surl)
            continue
        except Site.DoesNotExist:    
            Site.objects.create(
                site_url=surl,
                name=sname
            )

