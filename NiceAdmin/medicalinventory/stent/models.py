from django.db import models

PROCESS_STATUS =(

    (1,'Pending'),
    (2,'Executed'),
    )
RETURN_STATUS =(

    (1,'Pending'),
    (2,'Success'),
    (3,'Failed'),
    )
CALL_BACK_STATUS =(
    (1,'Pending'),
    (2,'Executed'),
)

class process_queue(models.Model):
    process_id                  =    models.IntegerField(primary_key=True, null=False)
    title                       =    models.CharField(max_length=200,null=False)
    process_file_location       =    models.TextField(null=False)
    process_status              =    models.IntegerField(choices=PROCESS_STATUS,default=1)
    return_status               =    models.IntegerField(choices=RETURN_STATUS,default=1)
    return_json                 =    models.TextField()
    call_back_url               =    models.CharField(max_length=200)
    call_back_status            =    models.IntegerField(choices=CALL_BACK_STATUS,default=1)
    call_back_json              =    models.TextField()
    process_entry_date          =    models.DateTimeField()

class company_settings(models.Model):
    CompanyTitle                =     models.CharField(max_length=255)
    CompanyAddressLine1         =     models.CharField(max_length=255)
    Website                     =     models.CharField(max_length=255)
    Contactno                   =     models.CharField(max_length=20)
    Pincode                     =     models.IntegerField() 
    Post                        =     models.CharField(max_length=255)
    Logo                        =     models.TextField()
    Pancard                     =     models.CharField(max_length=50)
    RegNo                       =     models.CharField(max_length=100)
    created_at                  =     models.DateTimeField()
    updates_at                  =     models.DateTimeField()

STATUS=(
    (1,'Activate'),
    (0,'Inactive'),
)
class company_bank_accounts(models.Model):
    Slno                        =    models.AutoField(primary_key=True)
    BankName                    =    models.CharField(max_length=200)
    BranchName                  =    models.CharField(max_length=200)
    BranchIFSC                  =    models.CharField(max_length=100)
    Account_no                  =    models.CharField(max_length=100)
    Status                      =    models.IntegerField(choices=STATUS) 
    created_at                  =    models.DateTimeField()
    updates_at                  =    models.DateTimeField()
    deleted_at                  =    models.DateTimeField()

class Category(models.Model):   
    Cat_id                  =       models.AutoField(primary_key=True,null=False)
    category_title          =       models.CharField(max_length=100,unique=True)
    Slug                    =       models.CharField(max_length=100,unique=True)
    Parent_category         =       models.IntegerField()

class Products(models.Model):
    Product_id              =       models.AutoField(primary_key=True,null=False)
    Product_title           =       models.CharField(max_length=100)
    Product_image           =       models.TextField()

class Product_attributes(models.Model):
    Attribute_id           =        models.AutoField(primary_key=True,null=False)
    Attribute_title        =        models.CharField(max_length=200)
    Attribute_value        =        models.CharField(max_length=200)

class contacts(models.Model):
    contact_id              =        models.AutoField(primary_key=True,null=False)
    contact_title           =        models.CharField(max_length=200)
    contact_address_line1   =        models.CharField(max_length=100)
    contact_address_line1   =        models.CharField(max_length=100)          
    Pincode                 =        models.IntegerField() 
    Contactno               =        models.CharField(max_length=20,unique=True)
    Email                   =        models.CharField(max_length=200)
    Post                    =        models.CharField(max_length=200)

class products_suppliers(models.Model):
    supplier_id             =        models.AutoField(primary_key=True,null=False)
    product_id              =        models.IntegerField(help_text='FK')
    category_id             =        models.IntegerField()

class purchase_order_master(models.Model):
    purchase_order_id               =         models.AutoField(primary_key=True,null=False)
    purchase_order_date             =         models.DateTimeField()
    purchase_order_supplier_id      =         models.IntegerField()
    Net_amount                      =         models.DecimalField(max_digits=10,decimal_places=2)
    SGST_amount                     =         models.DecimalField(max_digits=10,decimal_places=2) 
    CGST_amount                     =         models.DecimalField(max_digits=10,decimal_places=2) 
    Total                           =         models.DecimalField(max_digits=10,decimal_places=2) 

class purchase_order_details(models.Model):
    Purchase_order_details_id       =         models.AutoField(primary_key=True,null=False)
    Product_id                      =         models.IntegerField()        
    Unit_price                      =         models.DecimalField(max_digits=10,decimal_places=2)
    Quantity                        =         models.IntegerField()
    Total_price                     =         models.DecimalField(max_digits=10,decimal_places=2) 


    #def __str__(self) -> str:
        
