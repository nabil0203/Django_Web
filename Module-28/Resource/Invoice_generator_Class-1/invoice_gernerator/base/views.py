from django.shortcuts import render,redirect
from . models import *
from django.forms import formset_factory
from . forms import *


# Create your views here.
def invoice_list(request):
    invoices = Invoice.objects.all()  #select * from invoice
    return render(request, 'invoice_list.html', {'invoices':invoices})



def invoice_details(request, id):
    invoice = Invoice.objects.get(id=id)
    return render(request, 'invoice_details.html', {'invoice':invoice})



def create_invoice(request):
    itemFormSet = formset_factory(InvoiceItemForm, extra=1)

    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        formset = itemFormSet(request.POST)

        if invoice_form.is_valid() and formset.is_valid():
            invoice = invoice_form.save()

            for form in formset:
                item = form.save(commit=False)
                item.invoice = invoice
                item.save()

            return redirect('invoice_list')
        
    else:
        invoice_form = InvoiceForm()
        formset = itemFormSet()

    return render(request, 'create_invoice.html', {'invoice_form':invoice_form, 'formset':formset})


from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML

def invoice_pdf(request, id):
    invoice = Invoice.objects.get(id=id)
    print(invoice)
    template = get_template("invoice_pdf.html")
    html = template.render({'invoice':invoice})

    pdf = HTML(string=html).write_pdf()
    response = HttpResponse(pdf, content_type = 'application/pdf')
    response['Content-Disposition'] = f'filename=invoice_{invoice.id}.pdf'
    return response
