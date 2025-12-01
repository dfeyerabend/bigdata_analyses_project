"""
Arrakis Night - Plot Styling for Python
========================================

A dark theme for matplotlib, pandas, and seaborn plots that matches
the Arrakis Night color scheme from JetBrains IDEs and Quarto theme.

Design concept: "Rivers in the Desert"
- Bars/lines: Muted blues and greens like desert water
- Plot title: Peach like rocky outcrops (matches Quarto H2)
- Axis labels: Gold like sand dunes (matches Quarto H1)
- Axis ticks: Muted gray (recedes, reference only)

Usage:
------
    # Option 1: Import and call apply()
    import arrakis_night_style
    arrakis_night_style.apply()
    
    # Option 2: Import just the colors for custom use
    from arrakis_night_style import COLORS
    plt.plot(x, y, color=COLORS['river_teal'])

    # Option 3: Get a color palette for multiple series
    from arrakis_night_style import get_palette
    colors = get_palette(5)  # Get 5 colors

Author: Generated for Quarto reports with PySpark
"""

import matplotlib.pyplot as plt

# =============================================================================
# COLOR PALETTE - "Rivers in the Desert" theme
# =============================================================================

COLORS = {
    # Backgrounds
    'bg_dark': '#2B2927',       # Main background
    'bg_medium': '#2D2A2E',     # Secondary background
    'bg_light': '#302F2E',      # Elevated surfaces
    'bg_elevated': '#403E41',   # Cards, tooltips
    
    # Foregrounds
    'fg_primary': '#C6CBCC',    # Main text
    'fg_bright': '#FCFCFA',     # Bright text
    'fg_muted': '#939293',      # Muted/secondary text (axis ticks)
    'fg_dim': '#5B595C',        # Dim text, grid lines
    
    # Heading colors (matching Quarto theme)
    'title': '#CCA361',         # Gold - plot titles (like dunes)
    'label': '#D4A870',         # Sandy-Gold - axis labels (spice gold)
    'ticks': '#939293',         # Muted gray - axis ticks (recedes)
    
    # Legacy heading names for compatibility
    'heading_h1': '#CCA361',    # Gold - matches Quarto H1
    'heading_h2': '#D4A870',    # Sandy-Gold - matches Quarto H2
    'heading_h3': '#95D1BE',    # Mint - matches Quarto H3
    
    # Accent colors (sand/warm tones for emphasis)
    'gold': '#CCA361',          # Primary accent (spice gold)
    'sand': '#C4A55A',          # Sandy accent
    'peach': '#D19577',         # Rocky peach
    
    # === WATER PALETTE === (blues and greens like desert water)
    'river_teal': '#7BA898',    # Primary - river through desert
    'shallow_pool': '#6BA8B0',  # Light blue-green pool
    'deep_oasis': '#5B8A72',    # Deep desert spring
    'morning_mist': '#8BBAB0',  # Pale teal morning water
    'twilight_water': '#6A9AA8', # Blue-gray evening water
    'desert_spring': '#7CB5A0', # Fresh water green
    'deep_channel': '#4A8888',  # Darker teal channel
    'oasis_edge': '#9BC4B0',    # Lightest green edge
}

# =============================================================================
# COLOR CYCLE - Distinct water + sand palette
# =============================================================================
# Ordered for maximum visual distinction in multi-series plots
# Pattern: teal → light blue → dark blue → gold sand → green → dark green

COLOR_CYCLE = [
    '#7BA898',  # 1. River teal (primary - standard)
    '#8EC4D4',  # 2. Light blue (sky reflection)
    '#4A7088',  # 3. Dark blue (deep water)
    '#CCA361',  # 4. Golden sand (warm accent)
    '#8FBA70',  # 5. Green (oasis plants)
    '#4A7858',  # 6. Dark green (deep oasis)
    '#6BA8B0',  # 7. Shallow pool (secondary teal)
    '#D4A868',  # 8. Light sand (dunes)
    '#5A9A78',  # 9. Medium green
    '#7AA0B0',  # 10. Medium blue
]


def get_palette(n: int = None, include_accent: bool = True) -> list:
    """
    Get a list of colors from the Arrakis Night water palette.
    
    Parameters
    ----------
    n : int, optional
        Number of colors to return. If None, returns all colors.
        If n > len(COLOR_CYCLE), colors will repeat.
    include_accent : bool, default True
        If True, includes the gold sand accent in the palette.
        If False, returns only water (blue/green) colors.
    
    Returns
    -------
    list
        List of hex color strings.
    
    Example
    -------
        colors = get_palette(5)
        for i, color in enumerate(colors):
            plt.bar(i, values[i], color=color)
    """
    if include_accent:
        palette = COLOR_CYCLE.copy()
    else:
        # Water-only palette (exclude the gold accent at index 5)
        palette = [c for i, c in enumerate(COLOR_CYCLE) if i != 5]
    
    if n is None:
        return palette
    
    # Cycle through colors if n > available colors
    return [palette[i % len(palette)] for i in range(n)]


def get_water_palette(n: int = None) -> list:
    """
    Get only water colors (no sand accent).
    Convenience wrapper for get_palette(n, include_accent=False).
    """
    return get_palette(n, include_accent=False)


def apply(seaborn: bool = True) -> None:
    """
    Apply the Arrakis Night "Rivers in the Desert" theme.
    
    Visual hierarchy:
    - Plot title: Peach (like rocky outcrops)
    - Axis labels: Gold (like sand dunes)  
    - Axis ticks: Muted gray (recedes)
    - Data colors: Blues/greens (like water)
    
    Parameters
    ----------
    seaborn : bool, default True
        If True and seaborn is installed, also configure seaborn styling.
    
    Example
    -------
        import matplotlib.pyplot as plt
        import arrakis_night_style
        
        arrakis_night_style.apply()
        
        # Now all your plots will use the desert water theme!
        plt.plot([1, 2, 3], [1, 4, 9])
        plt.show()
    """
    
    # Start with dark background base
    plt.style.use('dark_background')
    
    # Override with Arrakis Night colors
    # Design: "Rivers in the Desert"
    # - Title: Peach (rocky outcrops)
    # - Axis labels: Gold (sand dunes)
    # - Ticks: Muted gray (recedes)
    # - Data: Water blues/greens
    
    plt.rcParams.update({
        # Figure
        'figure.facecolor': COLORS['bg_dark'],
        'figure.edgecolor': COLORS['bg_dark'],
        'figure.figsize': (10, 6),
        'figure.dpi': 100,
        
        # Axes
        'axes.facecolor': COLORS['bg_dark'],
        'axes.edgecolor': COLORS['fg_dim'],
        'axes.labelcolor': COLORS['label'],      # GOLD - like sand dunes
        'axes.titlecolor': COLORS['title'],      # PEACH - like rocky outcrops
        'axes.titleweight': 'bold',
        'axes.titlesize': 14,
        'axes.labelsize': 11,
        'axes.labelweight': 'medium',
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.prop_cycle': plt.cycler(color=COLOR_CYCLE),
        
        # Grid
        'axes.grid': True,
        'grid.color': COLORS['bg_elevated'],
        'grid.linestyle': '-',
        'grid.linewidth': 0.5,
        'grid.alpha': 0.7,
        
        # Ticks - MUTED GRAY (recedes, reference only)
        'xtick.color': COLORS['ticks'],
        'ytick.color': COLORS['ticks'],
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        
        # Text
        'text.color': COLORS['fg_primary'],
        'font.size': 11,
        
        # Legend
        'legend.facecolor': COLORS['bg_elevated'],
        'legend.edgecolor': COLORS['fg_dim'],
        'legend.labelcolor': COLORS['fg_primary'],
        'legend.fontsize': 10,
        'legend.framealpha': 0.9,
        
        # Lines
        'lines.linewidth': 2,
        'lines.markersize': 8,
        
        # Patches (bars, etc.)
        'patch.edgecolor': COLORS['bg_dark'],  # Subtle edge on bars
        
        # Savefig defaults
        'savefig.facecolor': COLORS['bg_dark'],
        'savefig.edgecolor': COLORS['bg_dark'],
        'savefig.bbox': 'tight',
        'savefig.dpi': 150,
    })
    
    # Configure seaborn if available and requested
    if seaborn:
        try:
            import seaborn as sns
            
            sns.set_theme(style="darkgrid", rc={
                'figure.facecolor': COLORS['bg_dark'],
                'axes.facecolor': COLORS['bg_dark'],
                'axes.edgecolor': COLORS['fg_dim'],
                'axes.labelcolor': COLORS['label'],
                'axes.titlecolor': COLORS['title'],
                'text.color': COLORS['fg_primary'],
                'xtick.color': COLORS['ticks'],
                'ytick.color': COLORS['ticks'],
                'grid.color': COLORS['bg_elevated'],
            })
            
            # Set the water color palette
            sns.set_palette(COLOR_CYCLE)
            
        except ImportError:
            pass  # Seaborn not installed, skip silently
    
    print("✓ Arrakis Night 'Rivers in the Desert' theme applied")
    print("  → Title: Peach | Labels: Gold | Ticks: Gray | Data: Water blues/greens")


def apply_to_figure(fig, ax=None) -> None:
    """
    Apply Arrakis Night styling to an existing figure.
    
    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure to style.
    ax : matplotlib.axes.Axes or list, optional
        Specific axes to style. If None, styles all axes in figure.
    """
    fig.set_facecolor(COLORS['bg_dark'])
    
    if ax is None:
        axes = fig.get_axes()
    elif isinstance(ax, list):
        axes = ax
    else:
        axes = [ax]
    
    for a in axes:
        a.set_facecolor(COLORS['bg_dark'])
        a.tick_params(colors=COLORS['ticks'])
        a.xaxis.label.set_color(COLORS['label'])
        a.yaxis.label.set_color(COLORS['label'])
        a.title.set_color(COLORS['title'])
        
        for spine in a.spines.values():
            spine.set_color(COLORS['fg_dim'])


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def style_dataframe_plot(ax, title: str = None) -> None:
    """
    Style a pandas DataFrame plot with Arrakis Night colors.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes returned by df.plot()
    title : str, optional
        Title for the plot
    """
    ax.set_facecolor(COLORS['bg_dark'])
    ax.figure.set_facecolor(COLORS['bg_dark'])
    
    ax.tick_params(colors=COLORS['ticks'])
    ax.xaxis.label.set_color(COLORS['label'])
    ax.yaxis.label.set_color(COLORS['label'])
    
    if title:
        ax.set_title(title, color=COLORS['title'], fontweight='bold')
    
    # Style legend if present
    legend = ax.get_legend()
    if legend:
        legend.get_frame().set_facecolor(COLORS['bg_elevated'])
        legend.get_frame().set_edgecolor(COLORS['fg_dim'])
        for text in legend.get_texts():
            text.set_color(COLORS['fg_primary'])
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(COLORS['fg_dim'])
    ax.spines['left'].set_color(COLORS['fg_dim'])


# =============================================================================
# DEMO
# =============================================================================

if __name__ == '__main__':
    import numpy as np
    
    apply()
    
    # Create sample plots showing the water palette
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Line plot - multiple water-colored series
    x = np.linspace(0, 10, 100)
    for i in range(5):
        axes[0, 0].plot(x, np.sin(x + i*0.5), label=f'Stream {i+1}', linewidth=2.5)
    axes[0, 0].set_title('Water Streams')
    axes[0, 0].set_xlabel('Distance')
    axes[0, 0].set_ylabel('Flow rate')
    axes[0, 0].legend()
    
    # Bar plot - water colors
    categories = ['Oasis A', 'Oasis B', 'Oasis C', 'Oasis D', 'Oasis E']
    values = [23, 45, 56, 78, 32]
    colors = get_palette(5)
    axes[0, 1].bar(categories, values, color=colors)
    axes[0, 1].set_title('Water Sources')
    axes[0, 1].set_xlabel('Location')
    axes[0, 1].set_ylabel('Volume')
    
    # Pie chart - water palette with gold accent
    axes[1, 0].pie(
        values, 
        labels=categories, 
        colors=get_palette(5),
        autopct='%1.1f%%',
        textprops={'color': COLORS['fg_primary']}
    )
    axes[1, 0].set_title('Water Distribution')
    
    # Horizontal bar - like your revenue chart
    axes[1, 1].barh(categories, values, color=get_palette(5))
    axes[1, 1].set_title('Revenue by Region')
    axes[1, 1].set_xlabel('Share of total (%)')
    
    plt.suptitle('Arrakis Night: Rivers in the Desert', 
                 fontsize=16, 
                 color=COLORS['gold'],
                 fontweight='bold')
    plt.tight_layout()
    plt.show()
