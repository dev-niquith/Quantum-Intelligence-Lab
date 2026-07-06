"""
main.py

Quantum Intelligence Lab (QIL)

Main application entry point.

Responsibilities
----------------

• Load dataset
• Execute unified research benchmark
• Display research comparison matrix
• Save benchmark results

Version
-------

QIL v1.0
"""

from src.benchmarking.research_benchmark import (
    ResearchBenchmark
)

from src.datasets.dataset_loader import (
    DatasetLoader
)


def main():
    """
    Main execution function.
    """

    print()

    print("=" * 60)
    print("QUANTUM INTELLIGENCE LAB")
    print("=" * 60)

    # ----------------------------------
    # Load Dataset
    # ----------------------------------

    #dataset_loader = DatasetLoader()
    #X, y = dataset_loader.load_dataset()


    #from src.config.config_manager import (
        #ConfigManager
    #)

    #config = ConfigManager()

    #dataset_config = config.get(
        #"dataset"
    #)

    #dataset_loader = DatasetLoader()

    #X, y = dataset_loader.load_dataset(

        #dataset_config["name"]

    #)



    # ----------------------------------
    # Initialize Benchmark Engine
    # ----------------------------------

    #benchmark = ResearchBenchmark(

        #folds=5,

        #random_seed=42

    #)






    from src.config.config_manager import ConfigManager

    # ----------------------------------
    # Load Configuration
    # ----------------------------------



    config = ConfigManager()

    dataset_name = config.get(
        "dataset.name"
    )

    folds = config.get(
        "cross_validation.folds"
    )

    random_seed = config.get(
        "random_seed"
    )

    # ----------------------------------
    # Load Dataset
    # ----------------------------------

    dataset_loader = DatasetLoader()

    X, y = dataset_loader.load_dataset(
        dataset_name
    )

    # ----------------------------------
    # Initialize Benchmark
    # ----------------------------------

    benchmark = ResearchBenchmark(
        folds=folds,
        random_seed=random_seed
    )




    # ----------------------------------
    # Execute Benchmark
    # ----------------------------------

    leaderboard = benchmark.execute(

        X,

        y,

        dataset_name=dataset_name

    )

    # ----------------------------------
    # Final Summary
    # ----------------------------------

    print()

    print("=" * 60)
    print("QIL EXECUTION COMPLETED")
    print("=" * 60)

    print()

    print(
        f"Models Evaluated : {len(leaderboard)}"
    )

    print(
        f"Best Model       : {leaderboard.iloc[0]['model']}"
    )

    print(
        f"Category         : {leaderboard.iloc[0]['category']}"
    )

    print(
        f"Accuracy         : "
        f"{leaderboard.iloc[0]['accuracy']:.4f}"
    )

    print()


if __name__ == "__main__":
    main()