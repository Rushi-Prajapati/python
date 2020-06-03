
import numpy as np 
import matplotlib.pyplot as plt 

product = ["bells", "whistles","books","pen","other"]

data = [23, 17, 35, 29, 12] 

explode = (0.1, 0.2, 0.3, 0.0, 0.0) 

colors = ( "orange", "cyan", "brown","grey", "indigo", "beige")          

wp = { 'linewidth' : 1, 'edgecolor' : "green" }

def func(pct, allvalues): 
    absolute = int(pct / 100.*np.sum(allvalues)) 
    return "{:.1f}%\n({:d} g)".format(pct, absolute) 
fig, ax = plt.subplots(figsize =(10, 7)) 
wedges, texts, autotexts = ax.pie(data,  
                                  autopct = lambda pct: func(pct, data), 
                                  explode = explode,  
                                  labels = product, 
                                  shadow = True, 
                                  colors = colors, 
                                  startangle = 90, 
                                  wedgeprops = wp, 
                                  textprops = dict(color ="magenta")) 

ax.legend(wedges, product, 
          title ="sales report", 
          loc ="center left", 
          bbox_to_anchor =(1, 0, 0.5, 1)) 
  
plt.setp(autotexts, size = 8, weight ="bold") 
ax.set_title("Customizing pie chart") 
  
# show plot 
plt.show() 