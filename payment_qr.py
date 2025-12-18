import qrcode

# Taking UPI ID as a input user

upi_id = input("Enter the UPI ID for the payment QR code: ").strip()

# upi://pay?pa=<UPI_ID>&pn=<NAME>&am=<AMOUNT>&cu=CURRENCY&tn=MESSAGE

phonepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
Googlepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
Naviaxis_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
Pop_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Creating QR codes for each payment app
phonepay_qr = qrcode.make(phonepay_url)
Googlepay_qr = qrcode.make(Googlepay_url)
paytm_qr = qrcode.make(paytm_url)
Naviaxis_qr = qrcode.make(Naviaxis_url) 
Pop_qr = qrcode.make(Pop_url)

# Saving the QR codes as image files
phonepay_qr.save("phonepay_qr.png")
Googlepay_qr.save("googlepay_qr.png")
paytm_qr.save("paytm_qr.png")
Naviaxis_qr.save("naviaxis_qr.png")
Pop_qr.save("pop_qr.png")

# Displaying the QR codes
phonepay_qr.show()
Googlepay_qr.show()
paytm_qr.show()
Naviaxis_qr.show()
Pop_qr.show()
