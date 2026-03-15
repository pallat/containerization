#include <microhttpd.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define PORT 8888

enum MHD_Result answer_to_connection(void *cls, struct MHD_Connection *connection, 
                         const char *url, const char *method, const char *version, 
                         const char *upload_data, size_t *upload_data_size, void **con_cls) {
    const char *page = "<html><body>Hello, World!</body></html>";
    struct MHD_Response *response;
    int ret;

    response = MHD_create_response_from_buffer(strlen(page), (void *)page, MHD_RESPMEM_PERSISTENT);
    ret = MHD_queue_response(connection, MHD_HTTP_OK, response);
    MHD_destroy_response(response);

    if (ret != MHD_YES) {
        return MHD_NO;
    }
    return MHD_YES;
}

int main() {
    struct MHD_Daemon *daemon;

    daemon = MHD_start_daemon(MHD_USE_SELECT_INTERNALLY, PORT, NULL, NULL, 
                              &answer_to_connection, NULL, MHD_OPTION_END);
    if (NULL == daemon) return 1;

    printf("Server running on port %d\n", PORT);
    while (1) {
        sleep(1);
    }

    MHD_stop_daemon(daemon);

    printf("Server stopped\n");
    return 0;
}
