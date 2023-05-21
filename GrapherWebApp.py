import streamlit as st
import matplotlib.pyplot as plt
import math
import numpy as np
import random
st.set_page_config(page_title="ElliGraph")
def plot_ellipse(a, b):
      x = st.slider("Enter x value:", min_value=0.1, max_value=10.0, step=0.1, value=1.0)
      if abs(x) > a:
        st.write("Error: x-value must be less than your a value but greater than -a")
        return
      y = b * math.sqrt(1 - (x**2 / a**2))#finds y value from x and b
      y = -y #Reflects, the 
    
      plt.plot(x, y, 'ro')
      plt.annotate("({:.2f}, {:.2f})".format(x, y), (x, y))
      y = b * math.sqrt(1 - (x**2 / a**2))
      
      plt.plot(x, y, 'ro')
      plt.annotate("({:.2f}, {:.2f})".format(x, y), (x, y))
  
      x = 0
      y = b
      plt.plot(x, y, 'ro')
      plt.annotate("({:.2f}, {:.2f})".format(x, y), (x, y))
      y = -y
      plt.plot(x, y, 'ro')
      plt.annotate("({:.2f}, {:.2f})".format(x, y), (x, y))
  
      x = a
      y = 0
      plt.plot(x, y, 'ro')
      plt.annotate("({:.2f}, {:.2f})".format(x, y), (x, y))
      x = -x
      plt.plot(x, y, 'ro')
      plt.annotate("({:.2f}, {:.2f})".format(x, y), (x, y))
  
def main():
    st.title("Elliptical Grapher")
    st.write("#### Made by ***Zion Ceus***")

    # Create sliders for 'a' and 'b'
    a = st.slider("Enter *a* value:", min_value=0.1, max_value=10.0, step=0.1, value=1.0)
    b = st.slider("Enter b value:", min_value=0.1, max_value=10.0, step=0.1, value=1.0)

    # Display the major and minor axis values
    major_axis = max(a, b)
    minor_axis = min(a, b)
    st.write("Major axis:", major_axis)
    st.write("Minor axis:", minor_axis)

    # Generate the plot
    t = np.linspace(0, 2 * np.pi, 100)
    plt.plot(a * np.cos(t), b * np.sin(t))
    plt.axis('equal')
    plot_ellipse(a, b)

    # Display the plot using Streamlit's pyplot function
    st.pyplot()

if __name__ == '__main__':
    main()