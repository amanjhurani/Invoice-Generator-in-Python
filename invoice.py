
from datetime import date
from datetime import datetime
from num2words import num2words
today = date.today()
date=today.strftime("%b-%d-%Y")
now = datetime.now()
time = now.strftime("%H:%M:%S")
import os

logo='''

░██████╗░█████╗░██████╗░██████╗░██████╗░███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
╚█████╗░███████║██████╔╝██████╔╝██████╔╝█████╗░░██████╔╝
░╚═══██╗██╔══██║██╔═══╝░██╔═══╝░██╔══██╗██╔══╝░░██╔═══╝░
██████╔╝██║░░██║██║░░░░░██║░░░░░██║░░██║███████╗██║░░░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░
'''
print(logo)
print("Hello Sir, Welcome to SAPPREP invoice program"+"\n")
clear_prd=open("log/product.ss",'w')
clear_prd.write(" ")
clear_prd.close()
id1=open("log/invoice.id",'r')
invoiceid=id1.read()
id1.close()
id2=open("log/invoice.id",'w')
id3=int(invoiceid) + 1
id2.write(str(id3))
id2.close()
Customer_id=invoiceid

Zoreza_email = input("Please Type Zoreza Email:-")
Zoreza_website = input("Please Type Zoreza Website:-")
Customer_name=input("Please type Customer Name:-")
Customer_contact=str(input("Please Type Customer Contact Mobile Number:-"))
Customer_gstin=str(input("Please Type Customer GSTIN:-"))
Customer_iecno=str(input("Please Type Customer IEC No.:-"))
if Customer_gstin=='':
      Customer_gstin="NA"
if Customer_iecno=='':
      Customer_iecno="NA"
print("Please Type Customer Address:-")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
Customer_addr = '-'.join(lines)
Customer_addr = Customer_addr.replace("-", "<br/>")
Customer_mode=input("Please Type Mode of payment done by customer:-")
Customer_orderID=input("Please Type the Order Id:-")
if Zoreza_email or Zoreza_website:
      customer_detail_html='''
    <main>
      <div class="row">
        <div class="col-sm-6"><strong>Date & Time:</strong> '''+str(date)+ "   " + str(time) +'''</div>
        <div class="col-sm-6 text-sm-right"> <strong>Invoice No:</strong>#00'''+str(invoiceid)+'''</div>
      </div>
      <hr>
      <div class="row">
        <div class="col-sm-6 text-sm-right order-sm-1"> <strong>Pay To:</strong>
          <address>
          Zoreza Global Business (P) Ltd.<br/>
          A-702, Millie Enclave, Marve Road,<br/> Orlem, Malad(W), Mumbai 400064<br/>
          <strong>Checkout Us: </strong><a href="https://www.sapprep.com">www.sapprep.com</a><br/>
          <strong>Email Us: </strong>info@sapprep.com<br/>
          <strong>Checkout Us: </strong><a href="https://"'''+str(Zoreza_website)+'''>'''+str(Zoreza_website)+'''</a><br/>
          <strong>Email Us: </strong>'''+str(Zoreza_email)+'''<br/>
          </address>
        </div>
        <div class="col-sm-6 order-sm-0"> <strong>Invoiced To:</strong>
          <address>
          '''+str(Customer_name)+'''<br /> +91-
        '''+str(Customer_contact)+'''<br />
          '''+Customer_addr+'''<br />
        <div class=""> <strong>Payment Mode:</strong> '''+str(Customer_mode)+'''</div>
        <strong>Order Id: </strong>'''+str(Customer_orderID)+'''<br/>
        <strong>GSTIN: </strong>'''+str(Customer_gstin)+'''<br/><strong>IEC No: </strong>'''+str(Customer_iecno)+'''
          </address>
        </div>
      </div> 
      <div class="card">
        <div class="card-body px-2" style="padding-top: 0px; padding-bottom: 0px;">
          <div class="table-responsive">
            <table class="table">
              <tbody>
              <tr>
            <th class="col-3 border-0"  style="padding-left: 11px;padding-top: 16px;"><strong>Products</strong></th>
            <th class="col-4 border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Description</strong></th>
            <th class="col-2 text-center border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Rate</strong></th>
            <th class="col-1 text-center border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Quantity</strong></th>
            <th class="col-2 text-center border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Amount</strong></th>
            <th class="col-2 text-center border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Tax</strong></th>
            <th class="col-2 text-center border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Tax Amount</strong></th>
            <th class="col-2 text-right border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Total Amount</strong></th>
              </tr>
    '''
else:
      customer_detail_html='''
 <main>
  <div class="row">
    <div class="col-sm-6"><strong>Date & Time:</strong> '''+str(date)+ "   " + str(time) +'''</div>
    <div class="col-sm-6 text-sm-right"> <strong>Invoice No:</strong>#00'''+str(invoiceid)+'''</div>
  </div>
  <hr>
  <div class="row">
    <div class="col-sm-6 text-sm-right order-sm-1"> <strong>Pay To:</strong>
      <address>
      Zoreza Global Business (P) Ltd.<br/>
      A-702, Millie Enclave, Marve Road,<br/> Orlem, Malad(W), Mumbai 400064<br/>
      <strong>Checkout Us: </strong><a href="https://www.sapprep.com">www.sapprep.com</a><br/>
      <strong>Email Us: </strong>info@sapprep.com<br/>
      </address>
    </div>
    <div class="col-sm-6 order-sm-0"> <strong>Invoiced To:</strong>
      <address>
      '''+str(Customer_name)+'''<br /> +91-
     '''+str(Customer_contact)+'''<br />
      '''+str(Customer_addr)+'''<br />
     <div class=""> <strong>Payment Mode:</strong> '''+str(Customer_mode)+'''</div>
     <strong>Order Id: </strong>'''+str(Customer_orderID)+'''<br/>
      <strong>GSTIN: </strong>'''+str(Customer_gstin)+'''<br/><strong>IEC No: </strong>'''+str(Customer_iecno)+'''
      </address>
    </div>
  </div> 
   <div class="card">
    <div class="card-body px-2" style="padding-top: 0px; padding-bottom: 0px;">
      <div class="table-responsive">
        <table class="table">
          <tbody>
          <tr>
            <th class="col-3 border-0"  style="padding-left: 11px;padding-top: 16px;"><strong>Products</strong></th>
            <th class="col-4 border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Description</strong></th>
            <th class="col-2 text-center border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Rate</strong></th>
            <th class="col-1 text-center border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Quantity</strong></th>
            <th class="col-2 text-center border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Amount</strong></th>
            <th class="col-2 text-center border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Tax</strong></th>
            <th class="col-2 text-center border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Tax Amount</strong></th>
            <th class="col-2 text-center border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Total Amount</strong></th>
          </tr>
'''



Customer_order=int(input("Please Type The number of items:-"))
products_record=" "
t_amount=0
t_tax = 0
t_amount_without_tax = 0
prod_total_with_tax = 0
i=1
while(i<=Customer_order):
  prod_name=input("Please Type the "+ str(i) +" product Name:-")
  prod_des=input("Please Type the "+ str(i) +" product description:-")
  prod_rate=int(input("Please Type the "+ str(i) +" product Rate:-"))
  prod_quantity=int(input("Please Type the "+ str(i) +" product Quantity:-"))
  prod_tax = int(input("Please type The "+ str(i) +" product tax in %:-"))
  prod_total=prod_rate*prod_quantity
  tax = (prod_total*prod_tax)/100
  prod_total_with_tax = prod_total + tax
  t_tax += tax
  t_amount_without_tax += prod_total
  t_amount=t_amount+int(prod_total_with_tax)
  products_record=str(products_record)+str("{"+str(prod_name)+","+str(prod_des)+","+str(prod_rate)+","+str(prod_quantity)+","+str(prod_total)+","+str(prod_tax)+"}")
  html_tr_code=''' <tr>
            <td>'''+str(prod_name)+'''</td>
            <td class="text-1">'''+str(prod_des)+'''</td>
            <td class="text-center">'''+str(prod_rate)+'''</td>
            <td class="text-center">'''+str(prod_quantity)+'''</td>
            <td class="text-center">'''+str(prod_total)+'''</td>
            <td class="text-center">'''+str(prod_tax)+"%"+'''</td>
            <td class="text-center">'''+str(tax)+'''</td>
            <td class="text-right">'''+str(prod_total_with_tax)+'''</td>
          </tr>
          '''
  log_products=open("log\\product.ss",'a',encoding="utf-8")
  log_products.write(str(html_tr_code))
  log_products.close()
  i=i+1

  # <tr>
  #             <td colspan="5" class="bg-light-2 text-right"><strong>Sub Total:</strong></td>
  #             <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(t_amount)+'''</td>
  #           </tr>
  #           <tr>
  #             <td colspan="5" class="bg-light-2 text-right"><strong>Total Tax:</strong></td>
  #             <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(t_tax)+'''</td>
  #           </tr>
  #           <tr>
total_html='''
          <tr>
              <td colspan="4" class="bg-light-2 text-right"><strong>Total:</strong></td>
              <td colspan="4" class="bg-light-2 text-center">'''+str(u"\u20B9")+str(t_amount_without_tax)+'''<p style="font-size:12px">'''+'('+str(num2words(t_amount_without_tax))+')'+'''<p></td>
            </tr>
            <tr>
              <td colspan="4" class="bg-light-2 text-right"><strong>Grand Total:</strong></td>
              <td colspan="4" class="bg-light-2 text-center">'''+str(u"\u20B9")+str(t_amount)+'''<p style="font-size:12px">'''+'('+str(num2words(t_amount))+')'+'''<p></td>
            </tr>
            
    '''

def html(data):
    f=open('print_invoice.html','w',encoding="utf-8")
    body=open('log\\body.ss','r')
    b1=str(body.read())
    footer=open('log\\footer.ss','r')
    f1=str(footer.read())
    tr_data=open("log\\product.ss",'r')
    main_contant=tr_data.read()
    code_html=(b1 + data + main_contant+ total_html + f1)
    f.write(code_html)
    f.close()
    body.close()
    footer.close()
    os.system('start print_invoice.html')

def record(id,name,mobile,address,mode,products,total):
  record_file=open("log\\invoice_record.txt",'a')
  record=str("[ #"+str(id)+","+str(date)+","+str(time)+","+str(name)+","+str(mobile)+","+str(address)+","+str(mode)+","+str(products)+", Total Paid="+str(total)+']')
  record_file.write(record)
  record_file.write("\n")
  record_file.close()


html(customer_detail_html)
Customer_addr = Customer_addr.replace("<br/>", " ")
Customer_addr = "["+Customer_addr+"]"
record(Customer_id,Customer_name,Customer_contact,Customer_addr,Customer_mode,products_record,t_amount)
