import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 定义颜色
colors = ['#E89DA0', '#88CEE6', '#F6C8A8', '#B2D3A4', '#9FBA95', '#E6CECF', '#B696B6']

# 数据整理
concentrations = [0, 2, 4, 8, 16, 32]

# IL-6数据 (pg/ml)
il6_data = {
    'blank': [None, None, None, None, None, None],
    'lps': [2101.314, None, None, None, None, None],
    'a': [None, 1773.38656, 968.478463, 1773.18227, 1003.39087, 1688.79223],
    'b': [None, 1619.62534, 1995.64563, 2008.89385, 1425.5476, 1137.23109],
    'c': [None, 1355.66815, 1778.37616, 1858.75784, 1186.32622, 1722.60907],
    'd': [None, 1413.32713, 1057.04905, 1533.58411, 1677.6247, 1683.07512]
}

il6_errors = {
    'blank': [None, None, None, None, None, None],
    'lps': [177.6413, None, None, None, None, None],
    'a': [None, 94.88056, 105.6005, 148.1165, 64.67726, 118.4461],
    'b': [None, 107.08, 143.3841, 132.775, 89.76318, 13.00642],
    'c': [None, 47.31719, 159.3441, 139.8799, 82.76498, 1.243697],
    'd': [None, 121.3653, 14.26303, 105.3298, 143.8805, 258.5571]
}

# Relative (%)数据
relative_data = {
    'a': [None, 84.394172, 46.089183, 84.38445, 47.750639, 80.36839],
    'b': [None, 77.076788, 94.971319, 95.601793, 67.837391, 54.119998],
    'c': [None, 64.515258, 84.631624, 88.45693, 56.456399, 81.977709],
    'd': [None, 67.259207, 50.304193, 72.982149, 79.836935, 80.096317]
}

relative_errors = {
    'a': [None, 4.515297, 5.025451, 7.048751, 3.077941, 5.636764],
    'b': [None, 5.095858, 6.823545, 6.318668, 4.27157, 0.618966],
    'c': [None, 2.25179, 7.583069, 6.656783, 3.938725, 0.059187],
    'd': [None, 5.776657, 0.678767, 5.01257, 6.847168, 12.30455]
}

# 图1：IL-6柱状图
fig1, ax1 = plt.subplots(figsize=(12, 6))

# 设置柱状图的宽度和位置
bar_width = 0.15
x_positions = np.arange(len(concentrations))

# 绘制0μM的blank和lps
ax1.bar(x_positions[0] - bar_width/2, il6_data['lps'][0], bar_width, 
        yerr=il6_errors['lps'][0], capsize=5, color=colors[0], label='LPS', alpha=0.8)

# 绘制其他浓度的a, b, c, d
for i, conc_idx in enumerate(range(1, len(concentrations))):
    x_pos = x_positions[conc_idx]
    
    # a组
    if il6_data['a'][conc_idx] is not None:
        ax1.bar(x_pos - 1.5*bar_width, il6_data['a'][conc_idx], bar_width, 
                yerr=il6_errors['a'][conc_idx], capsize=5, color=colors[1], 
                label='a' if i == 0 else '', alpha=0.8)
    
    # b组
    if il6_data['b'][conc_idx] is not None:
        ax1.bar(x_pos - 0.5*bar_width, il6_data['b'][conc_idx], bar_width, 
                yerr=il6_errors['b'][conc_idx], capsize=5, color=colors[2], 
                label='b' if i == 0 else '', alpha=0.8)
    
    # c组
    if il6_data['c'][conc_idx] is not None:
        ax1.bar(x_pos + 0.5*bar_width, il6_data['c'][conc_idx], bar_width, 
                yerr=il6_errors['c'][conc_idx], capsize=5, color=colors[3], 
                label='c' if i == 0 else '', alpha=0.8)
    
    # d组
    if il6_data['d'][conc_idx] is not None:
        ax1.bar(x_pos + 1.5*bar_width, il6_data['d'][conc_idx], bar_width, 
                yerr=il6_errors['d'][conc_idx], capsize=5, color=colors[4], 
                label='d' if i == 0 else '', alpha=0.8)

ax1.set_xlabel('Concentration (μM)', fontsize=12, fontweight='bold')
ax1.set_ylabel('IL-6 (pg/mL)', fontsize=12, fontweight='bold')
ax1.set_title('IL-6 Levels at Different Concentrations', fontsize=14, fontweight='bold')
ax1.set_xticks(x_positions)
ax1.set_xticklabels(concentrations)
ax1.legend(loc='upper right')
ax1.grid(axis='y', alpha=0.3, linestyle='--')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('/workspace/il6_bar_chart.png', dpi=300, bbox_inches='tight')
print("图1已保存: il6_bar_chart.png")

# 图2：Relative (%)曲线图
fig2, ax2 = plt.subplots(figsize=(10, 6))

# 只绘制2-32μM的数据（去除0μM）
conc_for_curve = concentrations[1:]  # [2, 4, 8, 16, 32]

# 绘制四条曲线
groups = ['a', 'b', 'c', 'd']
line_colors = [colors[1], colors[2], colors[3], colors[4]]  # 使用E89DA0后的颜色

for idx, group in enumerate(groups):
    # 提取该组的数据（去除None值）
    y_data = [relative_data[group][i] for i in range(1, len(concentrations))]
    y_errors = [relative_errors[group][i] for i in range(1, len(concentrations))]
    
    # 绘制曲线和误差棒
    ax2.errorbar(conc_for_curve, y_data, yerr=y_errors, 
                marker='o', markersize=8, capsize=5, capthick=2,
                linewidth=2.5, color=line_colors[idx], label=f'Group {group}',
                alpha=0.8)

ax2.set_xlabel('Concentration (μM)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Relative (%)', fontsize=12, fontweight='bold')
ax2.set_title('Relative Inhibition at Different Concentrations', fontsize=14, fontweight='bold')
ax2.set_xticks(conc_for_curve)
ax2.set_xticklabels(conc_for_curve)
ax2.legend(loc='best', frameon=True, shadow=True)
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_ylim(0, 110)

plt.tight_layout()
plt.savefig('/workspace/relative_line_chart.png', dpi=300, bbox_inches='tight')
print("图2已保存: relative_line_chart.png")

plt.show()
print("\n图表生成完成！")
