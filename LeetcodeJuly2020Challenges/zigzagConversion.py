import time

start = time.time()

class Solution:
    def convert(self, s, numRows):
        if (len(s) <= numRows) or (numRows <= 1):
            return s
        else:
            L = []
            for j in range(numRows):
##                print(j)
                
                if j == 0:
                    L.extend([s[i] for i in range(len(s)) if not i%(2*numRows - 2)])
                elif j == (numRows-1):
                    L.extend([s[i] for i in range(len(s)) if not i%(2*numRows - 2) - (2*numRows -(numRows + 1))])
                else:
                    L.extend([s[i] for i in range(len(s)) if not ((i%(2*numRows - 2) - j) and (i%(2*numRows - 2) - (2*numRows - 2 - j)))])
##                print(L)
            return "".join(L) #"  ".join(L)
##        return "".join([s[i] for i in range(len(s)) if not i%(2*numRows - 2) - 0]) \
##               + "".join([s[i] for i in range(len(s)) if not ((i%(2*numRows - 2) - 1) and (i%(2*numRows - 2) - (2*numRows - 3)))]) \
##               + "".join([s[i] for i in range(len(s)) if not i%(2*numRows - 2) - (2*numRows -(numRows + 1))])
        
    
inputs = "PAYPALISHIRING"
input2 = 'abcdefghijklmnopqrstuvwxyz'
input3 = "twttvdpljlfvnpuwdxsabnheyrwdpqdimyejbtvnhciwucuzbnzfcgldyjgpzlzojdzlzwyizievmbuoquvsagxapdprqrhaugntdnbevibhjvxzpstsarsswkjpdsrxyetdrwjogkxpgxqxrmpsfkmdwxszpjynnrtgoewupwmxteukqmevwqbsnttcdrssjnbzrzvivjfoqcbgofemwfglazodsiydvbemacvylcobepkuxqivxogxpwdieblzeqogsjeflvjskvojlxginnfdlknqlarrqfykoesczbwmwmvjjcrzryecjruwrmqkrowisomurignwdyihrhasldbczzvlpfffcpasbuklczhfypppwphjuknumjhbqmhsbjncdxphwxmwodoltvwnikjutrxjfgehprluqdbmaqlotzbowyeeknadgyomeuvwniqdlsslidcbcfsafwfpjhuqfjemfzithawtsqgatkexqwyxufndohvwsbiyastksrdnilpdytdqrdnnkarykoueqeeswxcrphezvtctphjikywuzptlfprxuwqstujkeplzjquaxfiidgeevzrdpjajfsbapnltcyuloqnmvywaeafccyfrhhamcdprqamtaigpywdvuzxabecddjwktwzvcomuqanqiwhiskdojconhtskcpwxnvsplgkbgzuoxbwpmbfxeumnnfzruvphthxeojiwiclgfjxtndrtzdgmiffccumvejcuukqeodktnkpcpgvoldawkfamcmigxmcrwswmwihluwnjeixslzoxhojjdtrcftudnsrjczwxxjgctgugfkdmanxdgqiolc"
#525

h = Solution()
print(h.convert(input3,525))

ass = "twttvdpljlfvnpuwdxsabnheyrwdpqdimyejbtvnhciwucuzbnzfcgldyjgpzlzojdzlzwyizievmbuoquvsagxapdprqrhaugntdnbevibhjvxzpstsarsswkjpdsrxyetdrwjogkxpgxqxrmpsfkmdwxszpjynnrtgoewupwmxteukqmevwqbsnttcdrssjnbczlrozivqigvdjxfnoaqmcdbkgfogfuegmtwcfggjlxaxzwozdcsjirysdnvdbuetmfaccrvtydljcjoobhexpokzulxsqxiivexjongwxuplwhdiiwembwlszwerqcomgxsgjiemfclmvajfskkwvaodjlloxvggipncnpfkdnltkkndqoleaqrkruqufcyjkeovemsucczcbfwfmiwmmgvdjzjtcrrdznrtyxejcfjgrlucwirwmiqjkoreoxwhitshopmvuurrizgfnnwndmyuiehxrfhbamsplwdbbxcozuzzvglbpkfgflfpcspvansxbwupkclkcszthhfnyopcpjpowdpkhsjiuhkwniuqmnjahqbuqmmohcsvbzjwntckdwxjpdhdwcxembwaoxdzoulvtdvwwynpigkijauttmraxqjrfpgdechmparhlhurqfdybcmcafqaleoatwzybvomwnyqeoelkunyacdtglynopmaebusvfwjnaijqpddlrszsvleiedgcdbiciffsxaafuwqfjpzjlhpueqkfjjuetmsfqzwiutxhrapwftlstqpgzautwkyekxiqjwhypxtucftnvdzoehhvpwrscbxiwysaesetqkesurodknyirlapkdnyntddrq"

end = time.time()
print(end - start)
        
