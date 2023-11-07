
import streamlit as st
import numpy as np

st.title("NumPy Operations")

# Displaying dependencies with exact versions
st.write("Streamlit v" + st.__version__)
st.write("NumPy v" + np.__version__)

# Generating a random array
st.header("np.random.rand()")
with st.echo():
    arr = np.random.rand(5, 5)
st.code(arr)

# Reshaping an array
st.header("np.reshape()")
with st.echo():
    arr_reshaped = np.reshape(arr, (25,))
st.code(arr_reshaped)

# Calculating the mean of an array
st.header("np.mean()")
with st.echo():
    arr_mean = np.mean(arr)
st.code(arr_mean)

# Calculating the maximum of an array
st.header("np.max()")
with st.echo():
    arr_max = np.max(arr)
st.code(arr_max)

# Calculating the minimum of an array
st.header("np.min()")
with st.echo():
    arr_min = np.min(arr)
st.code(arr_min)

# Calculating the sum of an array
st.header("np.sum()")
with st.echo():
    arr_sum = np.sum(arr)
st.code(arr_sum)

# Finding the index of the maximum value in an array
st.header("np.argmax()")
with st.echo():
    max_index = np.argmax(arr)
st.code(max_index)

# Finding the index of the minimum value in an array
st.header("np.argmin()")
with st.echo():
    min_index = np.argmin(arr)
st.code(min_index)

# Transposing an array
st.header("np.transpose()")
with st.echo():
    arr_transposed = np.transpose(arr)
st.code(arr_transposed)
