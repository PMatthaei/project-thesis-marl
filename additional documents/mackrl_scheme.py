[
    {
        'name': 'observations', 
        'shape': (30,), 
        'select_agent_ids': range(0, 3), 
        'dtype': <class 'numpy.float32'>, 
        'missing': nan
    }, 
    {
        'name': 'state', 
        'shape': (48,),
        'dtype': <class 'numpy.float32'>, 
        'missing': nan,
        'size': 48
    },
    {
        'name': 'actions_level1__sample0', 
        'shape': (1,), 
        'dtype': <class 'numpy.int32'>, 
        'missing': -1
    }, 
    {
        'name': 'actions_level2__sample0', 
        'shape': (1,), 
        'dtype': <class 'numpy.int32'>, 
        'missing': -1}, 
    {
        'name': 'actions_level2', 
        'shape': (1,), 
        'select_agent_ids': range(0, 3), 
        'dtype': <class 'numpy.int32'>, 
        'missing': -1
    }, 
    {
        'name': 'actions_level3', 
        'shape': (1,), 
        'select_agent_ids': range(0, 3), 
        'dtype': <class 'numpy.int32'>,
         'missing': -1
    }, 
    {
        'name': 'actions', 
        'shape': (1,), 
        'select_agent_ids': range(0, 3),
        'dtype': <class 'numpy.int32'>, 
        'missing': -1
    }, 
    {
        'name': 'actions_onehot', 
        'shape': (9,), 
        'select_agent_ids': range(0, 3), 
        'dtype': <class 'numpy.int32'>, 
        'missing': -1
    }, 
    {
        'name': 'avail_actions_active', 
        'shape': (10,), 
        'select_agent_ids': range(0, 3), 
        'dtype': <class 'numpy.int32'>, 
        'missing': -1
    }, 
    {
        'name': 'avail_actions',
        'shape': (10,), 
        'select_agent_ids': range(0, 3), 
        'dtype': <class 'numpy.int32'>, 
        'missing': -1
    }, 
    {
        'name': 'reward', 
        'shape': (1,), 
        'dtype': <class 'numpy.float32'>, 
        'missing': nan
    }, 
    {
        'name': 'agent_id', 
        'shape': (1,), 
        'dtype': <class 'numpy.int32'>, 
        'select_agent_ids': range(0, 3), 
        'missing': -1
    }, 
    {
        'name': 'agent_id_onehot', 
        'shape': (3,), 
        'dtype': <class 'numpy.int32'>, 
        'select_agent_ids': range(0, 3), 
        'missing': -1
    }, 
    {
        'name': 'policies_level1', 
        'shape': (3,), 
        'dtype': <class 'numpy.float32'>, 
        'missing': nan
    }, 
    {
        'name': 'policies_level2__sample0', 
        'shape': (83,), 
        'dtype': <class 'numpy.int32'>, 
        'missing': -1
    }, 
    {
        'name': 'policies_level3', 
        'shape': (10,), 
        'select_agent_ids': range(0, 3), 
        'dtype': <class 'numpy.float32'>, 
        'missing': nan
    }, 
    {
        'name': 'terminated', 
        'shape': (1,), 
        'dtype': <class 'bool'>, 
        'missing': False
    }, 
    {
        'name': 'truncated', 
        'shape': (1,), 
        'dtype': <class 'bool'>, 
        'missing': False
    }, 
    {
        'name': 'reset', 
        'shape': (1,), 
        'dtype': <class 'bool'>, 
        'missing': False
    },
    {
        'name': 'mackrl_epsilons_central', 
        'scope': 'episode', 
        'shape': (1,), 
        'dtype': <class 'numpy.float32'>, 
        'missing': nan
    }, 
    {
        'name': 'mackrl_epsilons_central_level1', 
        'scope': 'episode', 
        'shape': (1,), 
        'dtype': <class 'numpy.float32'>, 
        'missing': nan
    }, 
    {
        'name': 'mackrl_epsilons_central_level2', 
        'scope': 'episode', 
        'shape': (1,), 
        'dtype': <class 'numpy.float32'>, 
        'missing': nan
    }, 
    {
        'name': 'mackrl_epsilons_central_level3', 
        'scope': 'episode', 
        'shape': (1,), 
        'dtype': <class 'numpy.float32'>, 
        'missing': nan
    }]
