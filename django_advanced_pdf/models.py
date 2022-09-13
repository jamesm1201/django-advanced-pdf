from django.db import models
from django.template import Template, Context

from django_advanced_pdf.engine.report_xml import ReportXML


class PrintingTemplate(models.Model):
    name = models.CharField(max_length=128, unique=True)
    xml = models.TextField()

    def __str__(self):
        return self.name

    def make_pdf(self, context=None, add_doctype=True, object_lookup=None, background_images=None, **kwargs):
        if context is None:
            xml = self.xml
        else:
            t = Template(self.xml)
            c = Context(context)
            xml = t.render(c)
        report_xml = ReportXML(object_lookup=object_lookup, background_images=background_images, pager_kwargs=kwargs)
        return report_xml.load_xml_and_make_pdf(xml, add_doctype=add_doctype)
