from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib.auth import logout
import requests
from account.models import MyUser
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        data = requests.get("https://api.coincap.io/v2/assets")
        if data.text=="You exceeded your 200 request(s) rate limit of your FREE plan":
            btc_price=49000
            eth_price=3023
        else:
            data = data.json()
            data = data["data"]
            btc_price = int(str((data[0]["priceUsd"]))[:5])
            eth_price = int(str((data[1]["priceUsd"]))[:4])
        data = requests.get("https://free.currconv.com/api/v7/convert?q=USD_TRY&compact=ultra&apiKey=bd0dd3713dff14e2e75e")
        if "503" in data.text:
            usd_price = 13
            euro_price = 15
        else:
            usd_price = int((data.json())["USD_TRY"])
            euro_price = int((data.json())["EUR_TRY"])

        if request.user.is_authenticated:
            coinBalance = (btc_price*MyUser.objects.get(email=request.user.email).btcBalance*usd_price + eth_price*MyUser.objects.get(email=request.user.email).ethBalance*usd_price)
            moneyBalance = MyUser.objects.get(email=request.user.email).euroBalance*euro_price + MyUser.objects.get(email=request.user.email).trBalance + usd_price*MyUser.objects.get(email=request.user.email).usdBalance
            return render(request, 'index.html',{
                "earnings": coinBalance+moneyBalance- MyUser.objects.get(email=request.user.email).investingBalance,
                "coinBalance": coinBalance,
                "moneyBalance": moneyBalance,
                "balance": coinBalance+moneyBalance, 
                "btc": MyUser.objects.get(email=request.user.email).btcBalance,
                "eth": MyUser.objects.get(email=request.user.email).ethBalance,
                "usd": MyUser.objects.get(email=request.user.email).usdBalance,
                "euro": MyUser.objects.get(email=request.user.email).euroBalance,
                "tl": MyUser.objects.get(email=request.user.email).trBalance,
                "btc_balance": str(int(int(MyUser.objects.get(email=request.user.email).btcBalance)*btc_price*usd_price)/(coinBalance+moneyBalance)*100),
                "eth_balance": str(int(MyUser.objects.get(email=request.user.email).ethBalance*eth_price*usd_price)/(coinBalance+moneyBalance)*100),
                "usd_balance": str(int(MyUser.objects.get(email=request.user.email).usdBalance*usd_price)/(coinBalance+moneyBalance)*100),
                "eur_balance": str(int(MyUser.objects.get(email=request.user.email).euroBalance*euro_price)/(coinBalance+moneyBalance)*100),
                "try_balance": str(int(MyUser.objects.get(email=request.user.email).trBalance)/(coinBalance+moneyBalance)*100),
                "btc_price":btc_price,
                "btc_priceTRY":btc_price*usd_price,
                "btcBalanceTRY":btc_price*usd_price*MyUser.objects.get(email=request.user.email).btcBalance,
                "eth_price":eth_price,
                "eth_priceTRY":eth_price*usd_price,
                "ethBalanceTRY":eth_price*usd_price*MyUser.objects.get(email=request.user.email).ethBalance,
                "usd_price":usd_price,
                "usdBalanceTRY":usd_price*MyUser.objects.get(email=request.user.email).usdBalance,
                "euro_price":euro_price,
                "euro_priceUSD":euro_price/usd_price,
                "euroBalanceTRY":euro_price*MyUser.objects.get(email=request.user.email).euroBalance,
                "trBalance":1/usd_price,
                "tryBalance":MyUser.objects.get(email=request.user.email).trBalance/(coinBalance+moneyBalance)*100,
            })
        else:
            return redirect("login")

def logout_request(request):
    logout(request)
    return redirect("login")