from crewai_tools import SeleniumScrapingTool

class ScrapeTool():

  def scrape1(website):
    """"scrape content from the website"""
    
    return SeleniumScrapingTool('https://www.skillsfuture.gov.sg/initiatives/students/skills-framework')
  
  
  def scrape2(website):
    """"scrape content from the website"""
    
    return SeleniumScrapingTool('https://www.ite.edu.sg/admissions/full-time-courses/nitec-and-3-year-higher-nitec/progression-opportunities')
  

