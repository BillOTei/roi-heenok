import sys
import os

from cx_Freeze import setup, Executable

setup(
    name = "Roi",
    version = "1.0",
    description = "Le vrai pour ceux qui cherchent leur papa...",
    executables = [Executable("main.py")]
)