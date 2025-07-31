
import numpy as np

def find_unified_optimal_configuration(N_list, verbose=True):
    """
    找到最优的统一TPC配置（每个启用的GPC使用相同数量的TPC）
    
    参数:
        N_list: 长度为8的列表，表示GPC1~GPC8的损坏TPC数量
        verbose: 是否打印详细分析
        
    返回:
        best_config: 最优配置信息
        best_performance: 最佳性能指标
        enabled_gpcs: 启用的GPC索引列表
    """
    # 计算每个GPC的可用TPC
    TPC_list = [8 - N for N in N_list]
    
    # 初始化最佳配置
    best_performance = 0
    best_t = 0
    best_set = []
    
    # 遍历所有可能的统一TPC数量 (1到8)
    for t in range(1, 9):
        # 选择所有TPC_i >= t的GPC
        enabled_indices = [i for i, tpc in enumerate(TPC_list, 1) if tpc >= t]
        set_size = len(enabled_indices)
        
        # 计算性能指标 = GPC数量 × 统一TPC数量
        performance = set_size * t
        
        # 更新最佳配置（性能相同时选择更大的t值）
        if performance > best_performance or (performance == best_performance and t > best_t):
            best_performance = performance
            best_t = t
            best_set = enabled_indices
    
    # 结果分析
    if verbose:
        print("\n" + "="*60)
        print("统一TPC配置优化分析")
        print("="*60)
        print(f"GPC损坏情况: {N_list}")
        print(f"可用TPC: {TPC_list}")
        print(f"\n最优配置: 统一TPC数量 = {best_t}")
        print(f"启用的GPC: {sorted(best_set)}")
        print(f"禁用GPC: {sorted(set(range(1,9)) - set(best_set))}")
        print(f"性能指标: {best_performance:.2f} (处理速率)")
        
        # 性能比较
        full_perf = 8 * 8
        perf_percentage = (best_performance / full_perf) * 100
        print(f"\n性能对比: {perf_percentage:.1f}% 相对于完整芯片")
        
        # 文本可视化
        print("\n配置详情:")
        print("GPC索引 | 可用TPC | 启用状态 | 使用TPC")
        print("-------------------------------------")
        for i, tpc in enumerate(TPC_list, 1):
            status = "启用" if i in best_set else "禁用"
            used_tpc = best_t if i in best_set else 0
            print(f"{i:6}  | {tpc:7} | {status:8} | {used_tpc:7}")
    
    return {
        'unified_tpc': best_t,
        'performance': best_performance,
        'enabled_gpcs': sorted(best_set),
    }

def run_unified_test_cases():
    # 测试1: 7个完好，1个损坏2个TPC (GPC8)
    print("\n" + "="*60)
    print("测试用例1: 7个完好GPC，1个GPC损坏2个TPC")
    print("="*60)
    N_list1 = [0, 0, 0, 0, 0, 0, 0, 2]  # GPC8损坏2个TPC
    find_unified_optimal_configuration(N_list1)
    
    # 测试2: 6个完好，2个损坏2个TPC (GPC7和GPC8)
    print("\n" + "="*60)
    print("测试用例2: 6个完好GPC，2个GPC各损坏2个TPC")
    print("="*60)
    N_list2 = [0, 0, 0, 0, 0, 0, 2, 2]  # GPC7和8各损坏2个
    find_unified_optimal_configuration(N_list2)
    
    # 测试3: 混合损坏模式
    print("\n" + "="*60)
    print("测试用例3: 混合损坏模式")
    print("="*60)
    N_list3 = [1, 0, 3, 2, 0, 1, 2, 4]  # 各种损坏程度
    find_unified_optimal_configuration(N_list3)
    
    # 测试4: 全部轻微损坏
    print("\n" + "="*60)
    print("测试用例4: 所有GPC损坏1-2个TPC")
    print("="*60)
    N_list4 = [1, 2, 1, 2, 1, 2, 1, 2]
    find_unified_optimal_configuration(N_list4)
    
    # 测试5: 严重损坏情况
    print("\n" + "="*60)
    print("测试用例5: 严重损坏情况")
    print("="*60)
    N_list5 = [3, 6, 4, 8, 2, 5, 7, 1]  # 各种损坏程度
    find_unified_optimal_configuration(N_list5)

# 主程序
if __name__ == "__main__":
    run_unified_test_cases()
    
    # 自定义输入
    print("\n" + "="*60)
    print("自定义配置分析")
    print("="*60)
    print("请输入8个GPC的损坏TPC数量（空格分隔，0-8之间）:")
    
    while True:
        try:
            input_str = input("> ")
            if input_str.lower() == 'exit':
                break
                
            N_list = list(map(int, input_str.split()))
            if len(N_list) != 8:
                print("错误：需要8个数值")
                continue
                
            if any(n < 0 or n > 8 for n in N_list):
                print("错误：损坏TPC数量必须在0-8之间")
                continue
                
            find_unified_optimal_configuration(N_list)
            
        except ValueError:
            print("错误：请输入8个整数，空格分隔")
        except KeyboardInterrupt:
            break