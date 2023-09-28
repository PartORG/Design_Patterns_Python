"""
Chain of Responsibilities Pattern

Command Query Separation (CQS).

Idea is whenever we operate on objects
we separate all the invocations into two different
concepts: Query and Commands

Command -- something that you send when you are asking
for an action or change (please set your attack value to 2).

Query -- is asking for information (please give me your attack value).

CQS -- having separate means of sending commands and queries
to direct field access.
"""
