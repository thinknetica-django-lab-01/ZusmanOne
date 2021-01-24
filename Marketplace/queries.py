from main.models import Product,SaleMan,CategoryProduct,TagProduct

#Create
myboard = Product.objects.create(
    title_product='DC 123',
    description_product='самый лучший сноуборд в своем диапазоне',
    price_product=5000,
    saleman_product=SaleMan.objects.get(first_name='Burton'),
    category_product=CategoryProduct.objects.get(title_category='Snowboarding')

)

newskiing = Product.objects.create(
    title_product='new model 2021',
    description_product='лыжи для новичков',
    price_product=10000,
    saleman_product=SaleMan.objects.first(),
    category_product=CategoryProduct.objects.first()
)

sonboard = Product()

sonboard.title_product='burton-t56'
sonboard.description_product='сноуборд детский'
sonboard.price_product=3000
sonboard.saleman_product=SaleMan.objects.get(first_name ='K2')
sonboard.category_product=CategoryProduct.objects.get(title_category='Snowboarding')
sonboard.save()

#Filter
all_product=Product.objects.all()
snowboard_1=Product.objects.get(title_product='burton_t56')
only_snowboard=Product.objects.filter(category_product__title_category='Snowboarding')


