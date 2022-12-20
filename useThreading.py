'''from multiprocessing import Process
import sys

rocket = 0

def func1():
    global rocket
    print ('start func1')
    while rocket < sys.maxsize:
        rocket += 1
    print ('end func1')

def func2():
    global rocket
    print ('start func2')
    while rocket < sys.maxsize:
        rocket += 1
    print ('end func2')

if __name__=='__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()'''

import time 


url ="https://rr6---sn-gwpa-civy.googlevideo.com/videoplayback?expire=1671479294&ei=nWugY9zbM4T14-EPs7er0AE&ip=49.36.17.235&id=o-AAIVKeA2CCXz0GvD6Jg0Trfgw_H88USTnnb_lA5jOR5H&itag=140&source=youtube&requiressl=yes&mh=17&mm=31%2C29&mn=sn-gwpa-civy%2Csn-gwpa-qxae7&ms=au%2Crdu&mv=m&mvi=6&pl=22&pcm2=no&initcwndbps=210000&vprv=1&mime=audio%2Fmp4&ns=coUfqNUOypusoyZDDwELbJEK&gir=yes&clen=4040753&dur=249.614&lmt=1667080298791647&mt=1671457314&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5432434&n=If7IBNWvehia-x&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgDOrwuXvGJaiyg7LMPjnHnmaf6HpT1R3zbBH_l5hyeQwCIQDpZ0zpAaOaxwm_MwciESnCLHe6Ct3zl4QhCuPdxQzeXQ%3D%3D&sig=AOq0QJ8wRAIgOXI0yH0DJHkWt71X5YanOHlfK2-H02vCgQglxccOeR0CIDidGzfxTg8qblcuHXWGjHZxqd3e7gfRADx7VrUsmbzL"
import os


cmd = '''
curl 'https://rr6---sn-gwpa-civy.googlevideo.com/videoplayback?expire=1671479294&ei=nWugY9zbM4T14-EPs7er0AE&ip=49.36.17.235&id=o-AAIVKeA2CCXz0GvD6Jg0Trfgw_H88USTnnb_lA5jOR5H&itag=140&source=youtube&requiressl=yes&mh=17&mm=31%2C29&mn=sn-gwpa-civy%2Csn-gwpa-qxae7&ms=au%2Crdu&mv=m&mvi=6&pl=22&pcm2=no&initcwndbps=210000&vprv=1&mime=audio%2Fmp4&ns=coUfqNUOypusoyZDDwELbJEK&gir=yes&clen=4040753&dur=249.614&lmt=1667080298791647&mt=1671457314&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5432434&n=If7IBNWvehia-x&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgDOrwuXvGJaiyg7LMPjnHnmaf6HpT1R3zbBH_l5hyeQwCIQDpZ0zpAaOaxwm_MwciESnCLHe6Ct3zl4QhCuPdxQzeXQ%3D%3D&sig=AOq0QJ8wRAIgOXI0yH0DJHkWt71X5YanOHlfK2-H02vCgQglxccOeR0CIDidGzfxTg8qblcuHXWGjHZxqd3e7gfRADx7VrUsmbzL' \
  -H 'authority: rr6---sn-gwpa-civy.googlevideo.com' \
  -H 'accept: */*' \
  -H 'accept-language: en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'range: bytes=0-' \
  -H 'referer: https://rr6---sn-gwpa-civy.googlevideo.com/videoplayback?expire=1671479294&ei=nWugY9zbM4T14-EPs7er0AE&ip=49.36.17.235&id=o-AAIVKeA2CCXz0GvD6Jg0Trfgw_H88USTnnb_lA5jOR5H&itag=140&source=youtube&requiressl=yes&mh=17&mm=31%2C29&mn=sn-gwpa-civy%2Csn-gwpa-qxae7&ms=au%2Crdu&mv=m&mvi=6&pl=22&pcm2=no&initcwndbps=210000&vprv=1&mime=audio%2Fmp4&ns=coUfqNUOypusoyZDDwELbJEK&gir=yes&clen=4040753&dur=249.614&lmt=1667080298791647&mt=1671457314&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5432434&n=If7IBNWvehia-x&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgDOrwuXvGJaiyg7LMPjnHnmaf6HpT1R3zbBH_l5hyeQwCIQDpZ0zpAaOaxwm_MwciESnCLHe6Ct3zl4QhCuPdxQzeXQ%3D%3D&sig=AOq0QJ8wRAIgOXI0yH0DJHkWt71X5YanOHlfK2-H02vCgQglxccOeR0CIDidGzfxTg8qblcuHXWGjHZxqd3e7gfRADx7VrUsmbzL' \
  -H 'sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: video' \
  -H 'sec-fetch-mode: no-cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' \
  -H 'x-client-data: CIe2yQEIo7bJAQipncoBCLTtygEIlaHLAQiF+cwBCOv6zAEI8IDNAQi1gs0BCNSCzQEI74TNAQ==' \
  --compressed -o qui.mp3

'''

cmd1= f"google-chrome --headless --dump-dom {url}"

start = time.time()

os.system(cmd)



end = time.time()

total_time = end - start
print("\n"+ str(total_time))



