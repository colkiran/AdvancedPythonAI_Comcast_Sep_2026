
# one class too many responsibilities
class Report:

    def generate(self):
        pass

    def write_to_file(self):
        pass

    def send_mail(self):
        pass

# SRP - split the responsibilities

class ReportGeneration:
    def generate(self):
        pass

class ReportSaver:
    def generate(self):
        pass

class ReportMailer:
    def send_email(self):
        pass


    
