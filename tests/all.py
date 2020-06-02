# coding: utf8
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import logging
logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(name)s [%(levelname)s]: %(message)s",
)

import unittest
from integration.for_mysql.test_model_struct_mysql import TestModelStructMySQL
from integration.for_mysql.test_model_crud_mysql import TestModelCRUDMySQL
from integration.for_mysql.test_recordset_crud_mysql import TestRecordsetCRUDMySQL
from integration.for_mysql.test_relation_belongs_to_mysql import TestRelationBelongsToMysql
from integration.for_mysql.test_relation_reference_myself_mysql import TestRelationReferenceMyselfMysql
from integration.for_mysql.test_relation_has_many_mysql import TestRelationHasManyToMysql
from integration.for_mysql.test_relation_has_many_through_mysql import TestRelationHasManyThroughMysql
from integration.for_mysql.test_relation_has_one_mysql import TestHasOneToMysql
from integration.for_mysql.test_relation_has_one_through_mysql import TestRelationHasOneThroughMysql
from integration.for_mysql.test_relation_has_and_belongs_to_many_mysql import TestRelationHasAndBelongsToManyMysql
from integration.for_mysql.test_relation_include_mysql import TestRelationIncludeMysql
from integration.for_mysql.test_transaction_mysql import TestTransactionMysql

from unit.test_clauses import TestClauses
from unit.test_collection import TestCollection
from unit.test_filter import TestFilter
from unit.test_inflection import TestInflection
from unit.test_model_define import TestModelDefine

from unit.test_recordset_delete import TestRecordsetDelete
from unit.test_recordset_insert import TestRecordsetInsert
from unit.test_recordset_query import TestRecordsetQuery
from unit.test_recordset_update import TestRecordsetUpdate
from unit.test_relation_basic import TestRelationBasic

from unit.test_utils import TestUtils

from unit.test_validator_acceptance import TestValidatorAcceptance
from unit.test_validator_confirmation import TestValidatorConfirmation
from unit.test_validator_exclusion import TestValidatorExclusion
from unit.test_validator_format import TestValidatorFormat
from unit.test_validator_inclusion import TestValidatorInclusion
from unit.test_validator_length import TestValidatorLength
from unit.test_validator_numericality import TestValidatorNumericality
from unit.test_validator_presence import TestValidatorPresence


unit_tests = [
    TestClauses,
    TestCollection,
    TestFilter,
    TestInflection,
    TestModelDefine,

    TestRecordsetDelete,
    TestRecordsetInsert,
    TestRecordsetQuery,
    TestRecordsetUpdate,
    TestRelationBasic,
    TestUtils,

    TestValidatorAcceptance,
    TestValidatorConfirmation,
    TestValidatorExclusion,
    TestValidatorFormat,
    TestValidatorInclusion,
    TestValidatorLength,
    TestValidatorNumericality,
    TestValidatorPresence,
]


integration_tests = [
    TestTransactionMysql,

    TestRecordsetCRUDMySQL,
    TestModelStructMySQL,
    TestModelCRUDMySQL,

    TestRelationBelongsToMysql,
    TestRelationReferenceMyselfMysql,

    TestRelationHasManyToMysql,
    TestRelationHasManyThroughMysql,

    TestHasOneToMysql,
    TestRelationHasOneThroughMysql,

    TestRelationHasAndBelongsToManyMysql,

    TestRelationIncludeMysql
]


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) == 2 else 'all'
    if cmd not in ('all', 'unit', 'integration'):
        print ('python %s [all|unit|integration]' % sys.argv[0])
        sys.exit(-1)

    suite = unittest.TestSuite()
    if cmd == 'all' or cmd == 'unit':
        for t in unit_tests:
            suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(t))
    if cmd == 'all' or cmd == 'integration':
        for t in integration_tests:
            suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(t))

    unittest.TextTestRunner().run(suite)
