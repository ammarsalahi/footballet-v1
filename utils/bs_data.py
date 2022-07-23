
def set_v3(soup,context,lim):
    data=soup.find_all(class_='newsbox')
    count=0
    for d in data:
        if count<lim:
            context.append(
                {
                    'title':d.find(class_='title').text,
                    'caption':d.find(class_='caption').text,
                    'img':str(d.find('img')['src']),
                    'urlss':d.find(class_='news-cover-box')['href'],
                    'datess':d.find(class_='date').text.replace('-',''),
                }    
            )
        count+=1   

def set_ft(soup,context,lim):
    data=soup.find_all(class_='one-news',href=True)
    count=0
    for d in data:
        if count<lim:
            try:
                context.append(
                    {
                        'title':d.find(class_='text-container').find('h3').text,
                        'caption':d.find(class_='text-container').find('p').text,
                        'imgset':str(d.find('img')['srcset']),
                        'urlss':'https://footballi.net'+d['href'],
                        'datess':d.find('app-news-info').find(class_='news-info').find('time').text,
                    }    
                )
            except AttributeError:
                continue  
        count+=1      

def set_fn(soup,context,lim):
    data=soup.find_all('article')
    count=0
    for d in data:
        if count<lim:
            try:
                context.append(
                    {
                        'title':d.find(class_='col-7').find('h3').text,
                        'caption':d.find(class_='col-7').find('p').text,
                        'img':str(d.find('img')['src']),
                        'urlss':'https://www.farsnews.ir'+d.find(class_='col-5').find('a')['href'],
                        'datess':d.find(class_='col-7').find('span').text,
                    }    
                )
            except AttributeError:
                continue    
        count+=1    

def set_kv(soup,context,lim):
    data=soup.find_all(attrs={'data-conf':'{}'})
    count=0
    for d in data:
        if count<lim:
            try:
                context.append({
                        'title':d.find('h3').text,
                        'caption':d.find('p').text,
                        'img':str(d.find('img')['src']),
                        'urlss':'https://www.khabarvarzeshi.com'+d.find('a')['href'],
                        'datess':d.find('time').text,
                })
            except AttributeError:
                continue 
        count+=1           

def set_ts(soup,context,lim):
    data=soup.find_all(class_='list-item')
    count=0
    for d in data:
        if count<lim:
            try:
                context.append({
                    'title':d.find(class_='title').text,
                    'caption':d.find(class_='lead').text,
                    'img':str(d.find('img')['src']),
                    'urlss':'https://www.tasnimnews.com'+d.find('a')['href'],
                    'datess':d.find('time').text
                })
            except AttributeError:
                continue  
        count+=1          

def set_mh(soup,context,lim):
    data=soup.find_all(class_='news')
    count=0
    for d in data:
        if count<lim:
            try:
                context.append({
                    'title':d.find('h3').text,
                    'caption':d.find('p').text,
                    'img':str(d.find('img')['src']),
                    'datess':d.find('time').text,
                    'urlss':'https://www.mehrnews.com'+d.find('a')['href']
                })
            except AttributeError:
                continue
        count+=1    
  

def set_is(soup,context,lim):
    data=soup.find(class_='items').find_all('li')
    count=0
    for d in data:
        if count<lim:
            try:
                context.append({
                    'title':d.find('h3').text,
                    'caption':str(d.find('p').text),
                    'img':d.find('figure').find('img')['src'],
                    'urlss':'https://www.isna.ir'+d.find('a')['href'],
                    'datess':d.find('time').text
                })
            except AttributeError:
                continue
        count+=1    
  

def set_ko(soup,context,lim):
    data=soup.find(attrs={'id':'box202'}).find_all('li')
    count=0
    for d in data:
        if count<lim:
            try:
                context.append({
                    'title':d.find('h3').text,
                    'caption':str(d.find('p').text),
                    'img':str(d.find('img')['src']),
                    'urlss':'https://www.khabaronline.ir'+d.find('a')['href'],
                    'datess':d.find('time').text
                })
            except AttributeError:
                continue
        count+=1    

def set_ir(soup,context,lim):
    data=soup.find(attrs={'id':'box4'}).find_all('li')
    count=0
    for d in data:
        if count<lim:
            try:
                context.append({
                    'title':d.find('h3').text,
                    'caption':str(d.find('p').text),
                    'img':str(d.find('img')['src']),
                    'urlss':'https://www.irna.ir'+d.find('a')['href'],
                    'datess':d.find('time').text
                })
            except AttributeError:
                continue
        count+=1    


def set_im(soup,context,lim):
    data=soup.find_all(attrs={'data-conf':'{}'})
    count=0
    for d in data:
        if count<lim:
            try:
                context.append({
                        'title':d.find('h3').text,
                        'caption':d.find('p').text,
                        'img':str(d.find('img')['src']),
                        'urlss':'https://www.imna.ir'+d.find('a')['href'],
                        'datess':d.find('time').text,
                })
            except AttributeError:
                continue 
        count+=1        

def set_il(soup,context,lim):
    data=soup.find_all(class_='pr8')
    count=0
    for d in data:
        if count<lim:
            try:
                context.append({
                        'title':d.find('h3').text,
                        'caption':d.find('p').text,
                        'img':str(d.find('img')['src']),
                        'urlss':'https://www.ilna.ir'+d.find('a')['href'],
                        'datess':d.find('time').text,
                })
            except AttributeError:
                continue 
        count+=1       
