from setuptools import setup

package_name = 'onepub_twosub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='phs',
    maintainer_email='gus0tmd@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sum_calculator=onepub_twosub.fst_sub:main',
            'factorial_calculator=onepub_twosub.sec_sub:main',
            'onepub=onepub_twosub.one_pub:main',
        ],
    },
)
