# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# This stub exists to work around false MyPY errors in examples due to default_args handling.
# The difference in the stub file vs. original class are Optional args which are passed
# by default_args.
#
# TODO: Remove this file once we implement a proper solution (MyPy plugin?) that will handle default_args.

from typing import Optional

from airflow.providers.amazon.aws.hooks.eks import ClusterStates, FargateProfileStates, NodegroupStates
from airflow.providers.amazon.aws.sensors.eks import DEFAULT_CONN_ID  # type: ignore

class EksClusterStateSensor:
    def __init__(
        self,
        *,
        cluster_name: Optional[str] = None,
        target_state: ClusterStates = ClusterStates.ACTIVE,
        aws_conn_id: str = DEFAULT_CONN_ID,
        region: Optional[str] = None,
        **kwargs,
    ): ...

class EksFargateProfileStateSensor:
    def __init__(
        self,
        *,
        fargate_profile_name: str,
        cluster_name: Optional[str] = None,
        target_state: FargateProfileStates = FargateProfileStates.ACTIVE,
        aws_conn_id: str = DEFAULT_CONN_ID,
        region: Optional[str] = None,
        **kwargs,
    ): ...

class EksNodegroupStateSensor:
    def __init__(
        self,
        *,
        nodegroup_name: str,
        cluster_name: Optional[str] = None,
        target_state: NodegroupStates = NodegroupStates.ACTIVE,
        aws_conn_id: str = DEFAULT_CONN_ID,
        region: Optional[str] = None,
        **kwargs,
    ): ...