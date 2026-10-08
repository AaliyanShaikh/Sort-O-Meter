import streamlit as st
import pandas as pd
import plotly.express as px
from utils.visualization import get_sorting_steps
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort

from utils.data_generator import generate_data
from utils.benchmark import benchmark_algorithm


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Sort-O-Meter",
    page_icon="🏁",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🏁 Sort-O-Meter")

st.markdown(
    """
    ### The Sorting Algorithm Race

    Compare **Bubble Sort, Selection Sort, Insertion Sort,
    Merge Sort and Quick Sort** on the same dataset.
    """
)


# ============================================================
# ALGORITHMS
# ============================================================

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}


# ============================================================
# INPUT SECTION
# ============================================================

st.header("📥 Choose Your Dataset")

input_method = st.radio(
    "How do you want to provide the numbers?",
    [
        "Enter my own numbers",
        "Generate a dataset"
    ],
    horizontal=True
)


# ============================================================
# CUSTOM INPUT
# ============================================================

if input_method == "Enter my own numbers":

    st.subheader("✏️ Enter Numbers")

    user_input = st.text_input(
        "Enter numbers separated by commas",
        value="64, 25, 12, 22, 11, 90, 34, 7",
        placeholder="Example: 64, 25, 12, 22, 11, 90"
    )

    if st.button("📥 Load Numbers"):

        try:

            data = [
                int(x.strip())
                for x in user_input.split(",")
                if x.strip()
            ]

            if len(data) == 0:

                st.error("Please enter at least one number.")

            else:

                st.session_state.data = data

                st.success(
                    f"Successfully loaded {len(data)} numbers!"
                )

        except ValueError:

            st.error(
                "Invalid input! Please enter only numbers "
                "separated by commas."
            )


# ============================================================
# GENERATED DATASET
# ============================================================

else:

    st.subheader("🎲 Generate Dataset")

    data_size = st.number_input(
        "Number of elements",
        min_value=1,
        max_value=5000,
        value=10,
        step=1
    )

    data_type = st.selectbox(
        "Dataset Type",
        [
            "Random",
            "Sorted",
            "Reverse Sorted",
            "Nearly Sorted"
        ]
    )

    if st.button("🎲 Generate Dataset"):

        st.session_state.data = generate_data(
            int(data_size),
            data_type
        )

        st.success(
            f"Generated {data_size} numbers!"
        )


# ============================================================
# CHECK IF DATA EXISTS
# ============================================================

if "data" not in st.session_state:

    st.session_state.data = [
        64, 25, 12, 22, 11, 90, 34, 7
    ]


data = st.session_state.data


# ============================================================
# DISPLAY ORIGINAL DATA
# ============================================================

st.divider()

st.header("📦 Current Dataset")

st.write(
    f"**Number of elements:** {len(data)}"
)

if len(data) <= 100:

    st.code(str(data))

else:

    st.write("First 50 elements:")

    st.code(
        str(data[:50]) + " ..."
    )


# ============================================================
# SORTING SECTION
# ============================================================

st.divider()

st.header("🏎️ Sorting Algorithm Race")

if st.button(
    "🏁 START SORTING RACE",
    type="primary"
):

    results = []

    progress = st.progress(0)

    for index, (name, function) in enumerate(
        algorithms.items()
    ):

        result = benchmark_algorithm(
            function,
            data
        )

        results.append({
            "Algorithm": name,
            "Time (ms)": result["time"],
            "Comparisons": result["comparisons"],
            "Swaps": result["swaps"]
        })

        progress.progress(
            (index + 1) / len(algorithms)
        )

    st.session_state.results = pd.DataFrame(
        results
    )


# ============================================================
# SHOW RESULTS
# ============================================================

if "results" in st.session_state:

    results = st.session_state.results

    st.subheader("🏆 Race Results")

    st.dataframe(
        results.style.format({
            "Time (ms)": "{:.4f}"
        }),
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------------
    # WINNER
    # --------------------------------------------------------

    fastest = results.loc[
        results["Time (ms)"].idxmin()
    ]

    st.success(
        f"🏆 Fastest Algorithm: **{fastest['Algorithm']}** "
        f"with **{fastest['Time (ms)']:.4f} ms**"
    )

    # --------------------------------------------------------
    # TIME GRAPH
    # --------------------------------------------------------

    st.subheader("⏱️ Execution Time")

    fig = px.bar(
        results,
        x="Algorithm",
        y="Time (ms)",
        title="Execution Time Comparison",
        text_auto=".4f"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------------
    # COMPARISONS GRAPH
    # --------------------------------------------------------

    st.subheader("🔍 Comparisons")

    fig2 = px.bar(
        results,
        x="Algorithm",
        y="Comparisons",
        title="Number of Comparisons"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # --------------------------------------------------------
    # SWAPS GRAPH
    # --------------------------------------------------------

    st.subheader("🔄 Swaps / Moves")

    fig3 = px.bar(
        results,
        x="Algorithm",
        y="Swaps",
        title="Number of Swaps"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )


# ============================================================
# SEE ALL ALGORITHMS WORKING
# ============================================================

st.divider()

st.header("🔬 See All Algorithms Working")

st.write(
    "The same original dataset is passed through all five "
    "sorting algorithms."
)

if st.button("▶️ Sort Using All Algorithms"):

    sorting_results = {}

    for name, function in algorithms.items():

        sorted_data, comparisons, swaps = function(
            data
        )

        sorting_results[name] = sorted_data

    st.session_state.sorting_results = sorting_results


# ============================================================
# DISPLAY SORTED OUTPUT
# ============================================================

if "sorting_results" in st.session_state:

    sorting_results = st.session_state.sorting_results

    st.subheader("📊 Sorting Results")

    for name, sorted_data in sorting_results.items():

        st.markdown(
            f"### {name}"
        )

        if len(sorted_data) <= 100:

            st.code(
                " → ".join(
                    map(str, sorted_data)
                )
            )

        else:

            st.code(
                " → ".join(
                    map(str, sorted_data[:50])
                ) + " → ..."
            )

    # --------------------------------------------------------
    # VERIFY ALL RESULTS
    # --------------------------------------------------------

    all_same = len(
        {
            tuple(values)
            for values in sorting_results.values()
        }
    ) == 1

    if all_same:

        st.success(
            "✅ All five algorithms produced the same "
            "sorted result!"
        )

    else:

        st.error(
            "❌ The algorithms produced different results. "
            "Check the implementations."
        )


# ============================================================
# COMPLEXITY TABLE
# ============================================================

st.divider()

st.header("📚 Complexity Analysis")

complexity = pd.DataFrame({

    "Algorithm": [
        "Bubble Sort",
        "Selection Sort",
        "Insertion Sort",
        "Merge Sort",
        "Quick Sort"
    ],

    "Best Case": [
        "O(n)",
        "O(n²)",
        "O(n)",
        "O(n log n)",
        "O(n log n)"
    ],

    "Average Case": [
        "O(n²)",
        "O(n²)",
        "O(n²)",
        "O(n log n)",
        "O(n log n)"
    ],

    "Worst Case": [
        "O(n²)",
        "O(n²)",
        "O(n²)",
        "O(n log n)",
        "O(n²)"
    ],

    "Space": [
        "O(1)",
        "O(1)",
        "O(1)",
        "O(n)",
        "O(log n)"
    ]
})

st.dataframe(
    complexity,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# RECOMMENDATION
# ============================================================

st.divider()

st.header("🤖 Algorithm Recommendation")

if len(data) <= 20:

    st.info(
        "For a very small dataset, simple algorithms such as "
        "Insertion Sort are easy to use and understand."
    )

elif len(data) <= 1000:

    st.info(
        "For medium-sized datasets, Quick Sort or Merge Sort "
        "usually provide better performance."
    )

else:

    st.info(
        "For large datasets, prefer algorithms with "
        "O(n log n) average/worst-case performance such as "
        "Merge Sort."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Sort-O-Meter | DSA Mini Project | "
    "Comparative Analysis of Sorting Algorithms"
)
# ============================================================
# STEP-BY-STEP VISUALIZATION
# ============================================================

st.divider()

st.header("🎬 Step-by-Step Algorithm Visualization")

st.write(
    "Watch how each sorting algorithm transforms the "
    "same dataset step by step."
)

selected_algorithm = st.selectbox(
    "Choose an algorithm",
    [
        "Bubble Sort",
        "Selection Sort",
        "Insertion Sort",
        "Merge Sort",
        "Quick Sort"
    ]
)

if len(data) > 20:

    st.warning(
        "For visualization, use 20 or fewer numbers. "
        "Large datasets create too many steps."
    )

else:

    if st.button("🎬 Start Visualization"):

        steps = get_sorting_steps(
            selected_algorithm,
            data
        )

        st.session_state.visualization_steps = steps
        st.session_state.current_step = 0


    if "visualization_steps" in st.session_state:

        steps = st.session_state.visualization_steps

        current_step = st.session_state.get(
            "current_step",
            0
        )

        current = steps[current_step]

        st.subheader(
            f"Step {current_step + 1} / {len(steps)}"
        )

        st.info(
            f"**{current['message']}**"
        )

        st.code(
            " → ".join(
                map(str, current["array"])
            )
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            if st.button("⬅️ Previous"):

                if current_step > 0:

                    st.session_state.current_step -= 1
                    st.rerun()

        with col2:

            if st.button("➡️ Next"):

                if current_step < len(steps) - 1:

                    st.session_state.current_step += 1
                    st.rerun()

        with col3:

            if st.button("🔄 Restart"):

                st.session_state.current_step = 0
                st.rerun()