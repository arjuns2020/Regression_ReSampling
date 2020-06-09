import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    
setuptools.setup(
     name = 'reg_resampler',  
     version = '1.0',
     author = "Atif Hassan, Venkata Sai Krithik",
     author_email = "atif.hit.hassan@gmail.com, pvsaikrithik@gmail.com",
     description = "An interface to apply your favourite re-sampler on regression tasks.",
     long_description = long_description,
     long_description_content_type = "text/markdown",
     url = "https://github.com/atif-hassan/manual_spellchecker",
     py_modules = ["reg_resampler"],
     package_dir = {'': 'src'},
     install_requires = ["pandas", "scikit-learn", "numpy"],
     include_package_data = True,
     classifiers = [
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         'License :: OSI Approved :: BSD 3-Clause "New" or "Revised" License (BSD-3-Clause)',
         "Operating System :: OS Independent",
     ]
 )