from module.bili2txt.downloader import *
from module.bili2txt.totxet import *
from module.txt2txt.GLM import *


# 接受用户输入
url = 'https://www.bilibili.com/video/BV16ixcetExG/?t=11&spm_id_from=333.1007.tianma.2-1-4.click&vd_source=1fdeecac88e150072afd23de1421001e'

# bili2txt(url)


obj = D(url)
print('')
excuteCommand(f'ffmpeg -i ./runtime/{obj.audio} -q:a 0 -map a ./runtime/tmp-{obj.bv}.mp3 -y')
to_text(obj.bv)
