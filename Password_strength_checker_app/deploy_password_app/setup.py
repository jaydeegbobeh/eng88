setup(
    name="Password Analyser",
    version="1.0.0",
    description="Password analyser/ generator tools",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["package_tools"],
    include_package_data=True,
    install_requires=[

    ],
    entry_points={"console_scripts": ["app=password_functions:main"]},
)
