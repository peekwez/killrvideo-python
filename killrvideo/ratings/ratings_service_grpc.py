from concurrent import futures
import time

import grpc

import ratings_service_pb2
import ratings_service_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


#TODO refactor service implementation to separate class
def rate_video(video_id, user_id, rating):
    return

def get_rating(video_id):
    return #response body: video_id, ratings_count, ratings_total

def get_user_rating(video_id, user_id):
    return #response body: video_id, user_id, rating

class RatingsServiceServicer(ratings_service_pb2_grpc.RatingsServiceServicer):
    """Provides methods that implement functionality of the Ratings Service."""

    def __init__(self):
        print "started"
        return

    def RateVideo(self, request, context):
        """Rate a video
        """
        print request
        # TODO: implement service call
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
        # rate_video(request.video_id, request.user_id, request.rating)
        # TODO: publish UserRatedVideo event

    def GetRating(self, request, context):
        """Gets the current rating stats for a video
        """
        print request
        # TODO: implement service call
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
        # return get_rating(request.video_id)

    def GetUserRating(self, request, context):
        """Gets a user's rating of a specific video and returns 0 if the user hasn't rated the video
        """
        print request
        # TODO: implement service call
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
        # return get_user_rating(request.video_id,request. user_id)

# TODO: remove code for running this single service
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ratings_service_pb2_grpc.add_RatingsServiceServicer_to_server(
        RatingsServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    # only need this temporarily until such time as we're running multiple services?
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

