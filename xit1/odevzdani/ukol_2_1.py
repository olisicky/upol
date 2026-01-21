def decode_pixel(i, pr, pg, pb):

    # maska pro konkrétní kanály -> označí mi validní bity pro každý kanál
    b_mask = (1 << pb) - 1
    g_mask = ((1 << pg) - 1) << pb    # vytvoří jedničkovou masku, krerou musím pak posunout
    r_mask = ((1 << pr) - 1) << (pg + pb)

    r_val = (i & r_mask) >> (pg + pb)
    g_val = (i & g_mask) >> pb
    b_val = (i & b_mask)

    r = (r_val * 255) // ((1 << pr) - 1)
    g = (g_val * 255) // ((1 << pg) - 1)
    b = (b_val * 255) // ((1 << pb) - 1)
    
    return (r, g, b)


if __name__ == '__main__':
    parametrs = input("Zadejte parametry pr, pg, pb (oddělené čárkou): ")
    pr, pg, pb = map(int, parametrs.split(','))
    if pr + pg + pb != 8:
        raise ValueError("Součet parametrů musí být 8.")
    

    while True:
        user_input = input("Zadejte hodnotu pixelu (0-255) nebo 'konec' pro ukončení: ")
        if user_input.lower() == 'konec':
            break

        pixel_value = int(user_input)
        if not (0 <= pixel_value <= 255):
            print("Hodnota pixelu musí být v rozsahu 0-255.")
            continue
        print(decode_pixel(pixel_value, pr, pg, pb))



