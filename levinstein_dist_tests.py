import unittest
import top3groups
import Levenshtein as plp


class MyTestCase(unittest.TestCase):
    words1 = []
    words2 = []
    def get_lists(self):
        file1 = open("word_list_1.txt", "r")
        file2 = open("word_list_2.txt", "r")
        self.words1 = file1.readlines()
        self.words2 = file2.readlines()
        file1.close()
        file2.close()

    def test_distances(self):
        self.get_lists()
        for i in range(len(self.words1)):
            pred_dist = top3groups.LevinsteinDistance(self.words1[i], self.words2[i])
            print("Levinstain distance of words " + self.words1[i] + " and " + self.words2[i] + " is:")
            print(pred_dist.levinstein_dist())
            print(plp.distance(self.words1[i], self.words2[i]))
            #self.assertEqual(pred_dist.calc_dist_between_strings(), plp.distance(self.words1[i], self.words2[i]))




if __name__ == '__main__':
    unittest.main()

