import numpy as np
import scipy.stats as stats
import pandas as pd
#%pip install pandas scipy numpy
class HypothesisTester:
    def __init__(self, data):
        self.data = data

    def calculate_risk(self, feature_column, target_column='TotalClaims'):
        return self.data.groupby(feature_column)[target_column].mean()

    def calculate_margin(self, feature_column):
        return self.data.groupby(feature_column).apply(lambda x: x['TotalPremium'].sum() - x['TotalClaims'].sum())

    def chi_square_test(self, feature_column, target_column):
        contingency_table = pd.crosstab(self.data[feature_column], self.data[target_column])
        chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        return chi2, p_value

    def t_test(self, group1, group2):
        t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)
        return t_stat, p_value

    def one_way_anova(self, group_column, metric_column):
        groups = [group for _, group in self.data.groupby(group_column)[metric_column]]
        f_statistic, p_value = stats.f_oneway(*groups)
        return f_statistic, p_value

    def interpret_results(self, p_value, alpha=0.05):
        if p_value < alpha:
            return f"Reject the null hypothesis (p-value: {p_value:.4f}). There is a significant difference."
        else:
            return f"Fail to reject the null hypothesis (p-value: {p_value:.4f}). There is no significant difference."

    def perform_statistical_test(self, group_column, metric_column, test_type='anova'):
        groups = self.data[group_column].unique()

        if test_type == 'anova':
            statistic, p_value = self.one_way_anova(group_column, metric_column)
        elif test_type == 'chi_square':
            statistic, p_value = self.chi_square_test(group_column, metric_column)
        elif test_type == 't_test' and len(groups) == 2:
            group_a = self.data[self.data[group_column] == groups[0]][metric_column]
            group_b = self.data[self.data[group_column] == groups[1]][metric_column]
            statistic, p_value = self.t_test(group_a, group_b)
        else:
            return {
                "error": f"Unsupported test type '{test_type}' or incorrect number of groups for the test",
                "test_type": test_type,
                "statistic": None,
                "p_value": None,
                "interpretation": None
            }

        interpretation = self.interpret_results(p_value)

        return {
            "test_type": test_type,
            "statistic": statistic,
            "p_value": p_value,
            "interpretation": interpretation
        }
