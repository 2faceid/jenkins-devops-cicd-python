import fire

def hello(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)

def calculate_vat(name="price",name="vat_rate"):
    fire.Fire(vat_amount = fire.Fire(price * (vat_rate / 100)))
    fire.Fire(total_price = price + vat_amount)
    return vat_amount, total_price

fire.Fire(price = float(input("Enter the price: ")))
fire.Fire(vat_rate = float(input("Enter the VAT rate (%): ")))


vat_amount, total_price = calculate_vat(price, vat_rate)

print(f"VAT Amount: {vat_amount:.2f}")
print(f"Total Price (including VAT): {total_price:.2f}")
