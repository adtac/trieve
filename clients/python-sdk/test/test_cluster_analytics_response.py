# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.11.8
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_py_client.models.cluster_analytics_response import ClusterAnalyticsResponse

class TestClusterAnalyticsResponse(unittest.TestCase):
    """ClusterAnalyticsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClusterAnalyticsResponse:
        """Test ClusterAnalyticsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClusterAnalyticsResponse`
        """
        model = ClusterAnalyticsResponse()
        if include_optional:
            return ClusterAnalyticsResponse(
                clusters = [
                    trieve_py_client.models.search_cluster_topics.SearchClusterTopics(
                        avg_score = 1.337, 
                        created_at = '', 
                        dataset_id = '', 
                        density = 56, 
                        id = '', 
                        topic = '', )
                    ],
                queries = [
                    trieve_py_client.models.search_query_event.SearchQueryEvent(
                        created_at = '', 
                        dataset_id = '', 
                        id = '', 
                        latency = 1.337, 
                        query = '', 
                        query_rating = '', 
                        request_params = null, 
                        results = [
                            null
                            ], 
                        search_type = '', 
                        top_score = 1.337, 
                        user_id = '', )
                    ]
            )
        else:
            return ClusterAnalyticsResponse(
                clusters = [
                    trieve_py_client.models.search_cluster_topics.SearchClusterTopics(
                        avg_score = 1.337, 
                        created_at = '', 
                        dataset_id = '', 
                        density = 56, 
                        id = '', 
                        topic = '', )
                    ],
                queries = [
                    trieve_py_client.models.search_query_event.SearchQueryEvent(
                        created_at = '', 
                        dataset_id = '', 
                        id = '', 
                        latency = 1.337, 
                        query = '', 
                        query_rating = '', 
                        request_params = null, 
                        results = [
                            null
                            ], 
                        search_type = '', 
                        top_score = 1.337, 
                        user_id = '', )
                    ],
        )
        """

    def testClusterAnalyticsResponse(self):
        """Test ClusterAnalyticsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()