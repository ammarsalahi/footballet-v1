from bs_data import *
def set_mixed_data(model,context,soup):
        if model.name== 'ورزش سه':
            set_v3(soup=soup,context=context,lim=4)
        elif model.name== 'فوتبالی':
            set_ft(soup=soup,context=context,lim=4)
        elif model.name== 'فارس':
            set_fn(soup=soup,context=context,lim=4)
        elif model.name== 'خبرورزشی':
            set_kv(soup=soup,context=context,lim=4)
        elif model.name== 'تسنیم':
            set_ts(soup=soup,context=context,lim=4)
        elif model.name== 'مهر':
            set_mh(soup=soup,context=context,lim=4)
        elif model.name== 'ایسنا':
            set_is(soup=soup,context=context,lim=4)
        elif model.name== 'خبرآنلاین':
            set_ko(soup=soup,context=context,lim=4)    
        elif model.name== 'ایرنا':
            set_ir(soup=soup,context=context,lim=4) 
        elif model.name== 'ایمنا':
            set_im(soup=soup,context=context,lim=4)   
        elif model.name== 'ایلنا':
            set_il(soup=soup,context=context,lim=4)                            
def get_all_data(model,soup):
    soup=model.get_request()
    context=[]
    if model.name=='ورزش سه':
        set_v3(soup=soup,context=context,lim=15)
    elif model.name== 'فوتبالی':
        set_ft(soup=soup,context=context,lim=15)
    elif model.name== 'فارس':
        set_fn(soup=soup,context=context,lim=9)
    elif model.name== 'خبرورزشی':
            set_kv(soup=soup,context=context,lim=15)
    elif model.name== 'تسنیم':
        set_ts(soup=soup,context=context,lim=15)
    elif model.name== 'مهر':
        set_mh(soup=soup,context=context,lim=15)
    elif model.name== 'ایسنا':
        set_is(soup=soup,context=context,lim=15)
    elif model.name== 'خبرآنلاین':
        set_ko(soup=soup,context=context,lim=9)    
    elif model.name== 'ایرنا':
        set_ir(soup=soup,context=context,lim=15) 
    elif model.name== 'ایمنا':
        set_im(soup=soup,context=context,lim=9)   
    elif model.name== 'ایلنا':
        set_il(soup=soup,context=context,lim=9)       
    return context  