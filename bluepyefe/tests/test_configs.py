import os
import json
import glob

import bluepyefe as bpefe


def pytest_generate_tests(metafunc):
    """Generate config tests"""

    rootdir = os.path.dirname(os.path.abspath(__file__))
    configs_dir = os.path.join(rootdir, 'configs')

    config_paths = glob.glob(os.path.join(configs_dir, '*.json'))

    metafunc.parametrize("rootdir,config_path",
                         ((rootdir, config_path)
                          for config_path in config_paths), ids=config_paths)


def test_config(rootdir, config_path):
    """Test config"""

    config = json.load(open(config_path))

    config['path'] = os.path.join(rootdir, config['path'])

    extractor = bpefe.Extractor('test_run', config, use_git=False)
    extractor.create_dataset()
    extractor.plt_traces()
    extractor.extract_features(threshold=-30)
    extractor.mean_features()
    # extractor.analyse_threshold()
    extractor.plt_features()
    extractor.feature_config_cells()
    extractor.feature_config_all()
    extractor.plt_features_dist()

    '''
    extractor = bpefe.Extractor('testtype_legacy', config, use_git=False)
    extractor.create_dataset()
    extractor.plt_traces()
    extractor.extract_features(threshold=-30)
    extractor.mean_features()
    extractor.analyse_threshold()
    extractor.plt_features()
    extractor.feature_config_cells(version='legacy')
    extractor.feature_config_all(version='legacy')
    '''
