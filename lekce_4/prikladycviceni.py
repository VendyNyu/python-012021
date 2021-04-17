class Package:
    def __init__(self,address, weight):
        self.address = address
        self.weight = weight
        self.delivered = False
    def  deliver(self):
        self.delivered = True
    def get_info(self):
        return f'Adresa: {self.address}, Vaha: {self.weight}, Stav doručení: {self.delivered}'

class Driver:
        def __init__(self, name):
            self.name = name
            self.package_list= []

        def assign_package(self, package):
            if package.delivered:
                print('Balik nelze přiřadit už byl doručen.')
            else:
                self.package_list.append(package)
        #KOlik by měl doručit balíků - tolik kolik má v package listu
        def remaining_packages(self):
            return len(self.package_list)

balik = Package('Brno', 200)
balik2 = Package('Praha',200)

ridic = Driver('Martin')
print(ridic.remaining_packages())
ridic.assign_package(balik)
print(ridic.remaining_packages())
ridic.assign_package(balik2)
print(ridic.remaining_packages())








"""
class Employee:
  def takeHoliday(self, days):
    if self.remainingHolidayDays >= days:
      self.remainingHolidayDays -= days
      return f"Užij si to."
    else:
      return f"Bohužel už máš nárok jen na {self.remainingHolidayDays} dní."
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25

class PartTimeEmployee(Employee):
    def __init__(self, name, position, workload):
        super().__init__(name,position)
        self.workload = workload

    def get_info(self):
        return super().getInfo() + f"Uvazek: {self.workload}"

brigadnik = PartTimeEmployee('Karel','Udrzbar',0.5)
print(brigadnik.get_info())

"""

