from unicodedata import category
import numpy as np
import pandas as pd
import typer
from enum import Enum
import os

os.chdir("F:/Duke MIDS/706_Data Engineering Systems/Project2")


main = typer.Typer()


@main.command()
def hello(name: str):
    typer.echo(f"Hello {name}!")
    typer.echo(f"Welcome to the Cli interface for data preprocessing!")


@main.command()
def load_data(num: int = 5):
    """Load dataset"""
    """Type the number of rows you want to preview"""
    df = pd.read_csv("data.csv")
    df_head = df.head(num)
    typer.echo("Dataset loaded")
    typer.echo(df_head)


class feature_type(str, Enum):
    """feature type options"""

    categorical = "categorical"
    numeric = "numeric"


@main.command()
def show_features(type: feature_type):
    """Show features"""
    df = pd.read_csv("data.csv")
    categorical_features = df.select_dtypes(include=["object"]).columns
    numeric_features = df.select_dtypes(include=["int64", "float64"]).columns
    if type == "categorical":
        typer.echo("Categorical features shown")
        typer.echo(categorical_features)
    elif type == "numeric":
        typer.echo("Numeric features shown")
        typer.echo(numeric_features)


@main.command()
def show_label():
    """Show label"""
    df = pd.read_csv("data.csv")
    label = df["Survived"]
    typer.echo("Label shown")
    typer.echo(f"Percentage of people survived: {round(100 * label.mean(),2)}%")


@main.command()
def show_missing():
    """Show missing values"""
    df = pd.read_csv("data.csv")
    typer.echo("Missing values shown")
    typer.echo(df.isnull().sum())


if __name__ == "__main__":
    main()
