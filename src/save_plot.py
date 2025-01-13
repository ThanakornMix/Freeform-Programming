import os

def save_plot(fig, filename, save_graphs):
    """
    Save the given Matplotlib or Plotly figure to the graphs directory.
    :param fig: Matplotlib or Plotly figure object.
    :param filename: File name for saving the figure.
    :param save_graphs: Boolean flag to determine whether to save the graph.
    """
    if save_graphs:
        # Ensure the 'graphs' directory exists
        os.makedirs("graphs", exist_ok=True)
        
        filepath = os.path.join("graphs", filename)
        if hasattr(fig, 'savefig'):  # Matplotlib figure
            fig.savefig(filepath)
        elif hasattr(fig, 'write_html'):  # Plotly figure
            fig.write_html(filepath)
        print(f"Saved: {filepath}")
