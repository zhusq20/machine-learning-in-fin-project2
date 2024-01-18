import sys
import os

CHARAS_LIST = ['absacc','acc','age','agr','bm','bm_ia','cashdebt','cashpr','cfp','cfp_ia','chatoia','chcsho','chempia','chinv','chpmia','convind','currat','depr','divi','divo','dy','egr','ep','gma','grcapx','grltnoa','herf','hire','invest','lev','lgr','mve_ia','operprof','orgcap','pchcapx_ia','pchcurrat','pchdepr','pchgm_pchsale','pchquick','pchsale_pchinvt','pchsale_pchrect','pchsale_pchxsga','pchsaleinv','pctacc','ps','quick','rd','rd_mve','rd_sale','realestate','roic','salecash','saleinv','salerec','secured','securedind','sgr','sin','sp','tang','tb','aeavol','cash','chtx','cinvest','ear','ms','nincr','roaq','roavol','roeq','rsup','stdacc','stdcf','baspread','beta','betasq','chmom','dolvol','idiovol','ill','indmom','maxret','mom12m','mom1m','mom36m','mom6m','mvel1','pricedelay','retvol','std_dolvol','std_turn','turn','zerotrade']


# default learning rate of CA model
CA_DR = 0.5 # drop out rate
CA_LR = 0.001 # learning rate

# out of sample period
OOS_start = 19870101
OOS_end = 20211231



class HiddenPrints:
    def __init__(self, activated=True):
        self.activated = activated
        self.original_stdout = None

    def open(self):
        sys.stdout.close()
        sys.stdout = self.original_stdout

    def close(self):
        self.original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __enter__(self):
        if self.activated:
            self.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.activated:
            self.open()



def git_push(message):
    os.system('git add results')
    os.system(f'git commit -m "no_dropout: {message}"')
    os.system('git push')