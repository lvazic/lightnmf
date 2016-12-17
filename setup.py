from distutils.core import setup
setup(
  name = 'lightnmf',
  packages = ['lightnmf'],
  install_requires=[
          'numpy',
      ],
  version = '0.92',
  description = 'Simple Non-Negative Matrix Algorithm Implementation Using NumPy',
  author = 'Luka Vazic',
  author_email = 'lvazic@gmail.com',
  url = 'https://github.com/lvazic/simplenmf',
  download_url = 'https://github.com/lvazic/lightnmf/tarball/0.92',
  keywords = ['nmf', 'non-negative matrix factorization'],
  classifiers = [],
)