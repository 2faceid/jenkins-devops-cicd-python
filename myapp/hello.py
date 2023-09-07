import fire

def hello(name="World"):
  return "Hello %s!" % name


def calculate_vat(amount=1):
    tax_price = 17
    tax = (tax_price/100) * amount
    return tax

if __name__ == '__main__':
  fire.Fire(calculate_vat)



# fire.Fire(price = float(input("Enter the price: ")))
# fire.Fire(vat_rate = float(input("Enter the VAT rate (%): ")))


# vat_amount, total_price = calculate_vat(price, vat_rate)

# print(f"VAT Amount: {vat_amount:.2f}")
# print(f"Total Price (including VAT): {total_price:.2f}")
