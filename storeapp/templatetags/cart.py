from django import template

register = template.Library()

# jo product hain voh cart m hai k nhi 
@register.filter(name='is_in_cart') 
def is_in_cart(product,cart):

    keys = cart.keys()
    # jo product ki ID key ke id ke barabar hai ki nhi
    for id in keys:
        if int(id) == product.id:
            # print(id, product.id)
            # print(type(id), type(product.id))
            return True
    # print(keys)

    # console m product or product ki key or value print krwana ho toh
    # print(product,cart)
    # return True 
        
    return False
    
