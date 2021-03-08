#Výplata
#Složitejší řešení
class Employee:
  def get_tax(self):
      dan = self.salary * 0.15 - self.children * 1500
      return dan
  def get_net_salary(self):
      cisty_plat = self.salary - self.get_tax()
      return int(cisty_plat)

  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position, salary, children):
    self.name = name
    self.position = position
    self.salary = int(salary)
    self.children = int(children)

Zamestnanec1 = Employee("Harry Potter", "bystrozor", "50000", "3")
Zamestnanec2 = Employee("Hermiona Weasley", "ministryně magie", "100000","2")
Zamestnanec3 = Employee("Draco Malfoy", "úředník", "30000", "1")

print(f"{Zamestnanec1.get_info()} Jeho čistý plat je {Zamestnanec1.get_net_salary()}.")
print(f"{Zamestnanec2.get_info()} Její čistý plat je {Zamestnanec2.get_net_salary()}.")
print(f"{Zamestnanec3.get_info()} Jeho čistý plat je {Zamestnanec3.get_net_salary()}.")


"""
#Jednoduché řešení 

class Employee:
  def get_net_salary(self):
      cisty_plat = self.salary - (self.salary * 0.15 - self.children * 1500)
      return int(cisty_plat)

  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position, salary, children):
    self.name = name
    self.position = position
    self.salary = int(salary)
    self.children = int(children)

Zamestnanec1 = Employee("Harry Potter", "bystrozor", "50000", "3")
Zamestnanec2 = Employee("Hermiona Weasley", "ministryně magie", "100000","2")
Zamestnanec3 = Employee("Draco Malfoy", "úředník", "30000", "1")

print(f"{Zamestnanec1.get_info()} Jeho čistý plat je {Zamestnanec1.get_net_salary()}.")
print(f"{Zamestnanec2.get_info()} Její čistý plat je {Zamestnanec2.get_net_salary()}.")
print(f"{Zamestnanec3.get_info()} Jeho čistý plat je {Zamestnanec3.get_net_salary()}.")
"""


