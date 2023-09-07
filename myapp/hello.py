import fire

def hello(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)

def calculate_vat(price, vat_rate):
    vat_amount = price * (vat_rate / 100)
    total_price = price + vat_amount
    return vat_amount, total_price

price = float(input("Enter the price: "))
vat_rate = float(input("Enter the VAT rate (%): "))

vat_amount, total_price = calculate_vat(price, vat_rate)

print(f"VAT Amount: {vat_amount:.2f}")
print(f"Total Price (including VAT): {total_price:.2f}")
