import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America' , data))
  labels, values= utils.world_population(data)
  charts.generate_pie_chart(labels, values)
  
if __name__ == '__main__':
  run()

