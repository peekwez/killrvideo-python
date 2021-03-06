# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from comments import comments_service_pb2 as comments_dot_comments__service__pb2


class CommentsServiceStub(object):
  """Manages comments
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CommentOnVideo = channel.unary_unary(
        '/killrvideo.comments.CommentsService/CommentOnVideo',
        request_serializer=comments_dot_comments__service__pb2.CommentOnVideoRequest.SerializeToString,
        response_deserializer=comments_dot_comments__service__pb2.CommentOnVideoResponse.FromString,
        )
    self.GetUserComments = channel.unary_unary(
        '/killrvideo.comments.CommentsService/GetUserComments',
        request_serializer=comments_dot_comments__service__pb2.GetUserCommentsRequest.SerializeToString,
        response_deserializer=comments_dot_comments__service__pb2.GetUserCommentsResponse.FromString,
        )
    self.GetVideoComments = channel.unary_unary(
        '/killrvideo.comments.CommentsService/GetVideoComments',
        request_serializer=comments_dot_comments__service__pb2.GetVideoCommentsRequest.SerializeToString,
        response_deserializer=comments_dot_comments__service__pb2.GetVideoCommentsResponse.FromString,
        )


class CommentsServiceServicer(object):
  """Manages comments
  """

  def CommentOnVideo(self, request, context):
    """Add a new comment to a video
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUserComments(self, request, context):
    """Get comments made by a user
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetVideoComments(self, request, context):
    """Get comments made on a video
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CommentsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CommentOnVideo': grpc.unary_unary_rpc_method_handler(
          servicer.CommentOnVideo,
          request_deserializer=comments_dot_comments__service__pb2.CommentOnVideoRequest.FromString,
          response_serializer=comments_dot_comments__service__pb2.CommentOnVideoResponse.SerializeToString,
      ),
      'GetUserComments': grpc.unary_unary_rpc_method_handler(
          servicer.GetUserComments,
          request_deserializer=comments_dot_comments__service__pb2.GetUserCommentsRequest.FromString,
          response_serializer=comments_dot_comments__service__pb2.GetUserCommentsResponse.SerializeToString,
      ),
      'GetVideoComments': grpc.unary_unary_rpc_method_handler(
          servicer.GetVideoComments,
          request_deserializer=comments_dot_comments__service__pb2.GetVideoCommentsRequest.FromString,
          response_serializer=comments_dot_comments__service__pb2.GetVideoCommentsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'killrvideo.comments.CommentsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
